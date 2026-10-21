import os
from pymongo.mongo_client import MongoClient

C1 = MongoClient(os.environ["MONGODB_URI_3"])

C2 = MongoClient(os.environ["MONGODB_URI_4"])

C3 = MongoClient(os.environ["MONGODB_URI_5"])

myData = C3['test']['test']
print(list(myData.find({"Function" : "Software"})))