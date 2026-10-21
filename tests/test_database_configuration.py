"""Check connection configuration without importing or contacting the database."""
import ast
import os
from pathlib import Path
import re
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
CONNECTION_FILES = ("main.py", "MongoData.py", "MultiMong.py", "test.py")


class DatabaseConfigurationTests(unittest.TestCase):
    def connection_calls(self):
        for name in CONNECTION_FILES:
            source = (ROOT / name).read_text()
            tree = ast.parse(source, filename=name)
            calls = [node for node in ast.walk(tree)
                     if isinstance(node, ast.Call)
                     and isinstance(node.func, ast.Name)
                     and node.func.id == "MongoClient"]
            self.assertTrue(calls, name)
            for call in calls:
                yield name, source, call

    def test_no_embedded_credentials(self):
        pattern = r"mongodb(?:\+srv)?://[^\s'\"]*:[^\s'\"]*@"
        for name in CONNECTION_FILES:
            self.assertIsNone(re.search(pattern, (ROOT / name).read_text()), name)

    def test_missing_configuration_never_constructs_client(self):
        for name, _, call in self.connection_calls():
            client = Mock()
            expression = ast.Expression(body=call)
            with self.subTest(file=name, line=call.lineno), patch.dict(os.environ, {}, clear=True):
                with self.assertRaises(KeyError):
                    eval(compile(expression, name, "eval"), {"os": os, "MongoClient": client})
                client.assert_not_called()

    def test_explicit_configuration_is_forwarded_unchanged(self):
        settings = {"MONGODB_URI": "mongodb://127.0.0.1:27017"}
        settings.update({f"MONGODB_URI_{n}": f"mongodb://127.0.0.1:{27017+n}" for n in range(2, 6)})
        for name, _, call in self.connection_calls():
            client = Mock()
            expression = ast.Expression(body=call)
            with self.subTest(file=name, line=call.lineno), patch.dict(os.environ, settings, clear=True):
                eval(compile(expression, name, "eval"), {"os": os, "MongoClient": client})
                client.assert_called_once()
                self.assertIn(client.call_args.args[0], settings.values())


if __name__ == "__main__":
    unittest.main()
