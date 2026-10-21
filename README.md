# Supplier Performance — SirionLab Backend

A team hackathon prototype for supplier search and predictive performance analysis. The project explores domain search, company history, top-N selection and cost-trend prediction using FastAPI, MongoDB and scikit-learn.

The competition work used a **7m+ record dataset**; this is a record count, not a claim of seven million distinct real-world suppliers. The repository includes generated-data experiments and historical sample datasets. No reproducible sub-second performance benchmark is provided, and this prototype is not a production procurement recommendation service.

[Historical frontend](https://supper.netlify.app/) · [Project demonstration](https://www.youtube.com/watch?v=7FV2tm_gPM0)

The frontend link and demonstration are historical project context. A reachable frontend does not guarantee that the original API/database deployment is still operating.

## What the API does

| Endpoint | Input | Purpose |
| --- | --- | --- |
| `POST /domainSearch` | `{"SearchedString":"Software"}` | Return up to three records matching the `Function` field |
| `POST /companySearch` | `{"SearchedString":"Example supplier"}` | Retrieve a matching supplier record |
| `POST /predictionSearch` | `{"SearchedString":"Example supplier"}` | Fit a degree-five polynomial to historical cost values and return a normalized historical/projection series |
| `POST /numberSearch` | `{"No_of_Companies":3}` | Return the first N records from the collection; this route does not independently sort/rank every supplier |

The prediction code retains its original 2023–2024 projection horizon. Treat it as a historical modeling experiment, not a current forecast. Inputs and error handling require further work for empty datasets, missing companies, insufficient history and degenerate ranges.

![Project interface](https://user-images.githubusercontent.com/69640722/187020799-166d3bc9-706f-4ca3-b1fb-efd8f968d2c9.png)

## Configuration

**Use your own database.** Current source reads connection strings from required environment variables. It never supplies a default remote cluster or credentials. The scripts do not automatically load a `.env` file; `.env.example` lists placeholder variable names only. Missing variables stop the relevant script with a `KeyError` naming the missing setting.

| Script | Required environment variables | Behavior |
| --- | --- | --- |
| `main.py` | `MONGODB_URI` | API reads the `Test.Test` collection |
| `MongoData.py` | `MONGODB_URI_2` | Historical loader inserts local pickle data into `Test.Test` |
| `MultiMong.py` | `MONGODB_URI_2`, `MONGODB_URI_3`, `MONGODB_URI_4`, `MONGODB_URI_5` | Historical loader writes to four configured collections |
| `test.py` | `MONGODB_URI_3`, `MONGODB_URI_4`, `MONGODB_URI_5` | Historical database query script; not an automated unit-test suite |

Old Git commits still contain connection credentials. Removing them from current source does **not** revoke them or remove history. The database owners must revoke/rotate any credentials that remain valid; old credentials must not be reused. No old database connection was attempted for this maintenance change.

## Development setup

This is a Python 3.10-era dependency snapshot. The complete application dependency installation and database-backed behavior have not been revalidated on modern Python. Use an isolated environment and update dependencies before deploying a public service.

```sh
git clone https://github.com/chethanreddy123/SirionLab-Backend.git
cd SirionLab-Backend
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export MONGODB_URI='mongodb://127.0.0.1:27017'
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

The example uses a local MongoDB address without credentials; start your own MongoDB instance and populate suitable records first. The API expects fields including `SupplierName`, `Function`, `Cost` and `Year` in `Test.Test`. Empty or incomplete data will not support all routes. Do not run the historical loaders against a production database: they write records, depend on `CostAddedData/` files not fully provided here, and deserialize pickle inputs. Only load trusted local pickle data.

Open `http://127.0.0.1:8000/docs` for the API schema. No current hosted backend is promised.

## Network-free configuration checks

```sh
python -m unittest discover -s tests -v
```

These standard-library checks verify that the four connection scripts contain no embedded credential-bearing MongoDB URI, require explicit environment settings before constructing a client, and forward configured values unchanged. They do not import the application, install third-party dependencies, connect to MongoDB, validate model accuracy or constitute full API tests.

## Limitations and contribution scope

This repository is a team competition project. It preserves the original search/prediction logic rather than claiming modern agentic functionality. There is no authentication, rate limiting, current forecasting validation or production SLA. CORS and input handling need review before public exposure. The notebooks, datasets and generated caches are historical artifacts; they are not required evidence of a production system.

No repository-wide license grant is currently specified. Confirm the rights for team code and bundled assets before selecting licensing terms.
