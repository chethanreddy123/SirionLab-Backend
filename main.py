from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import joblib
import json
import pickle

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



Loaded_Content = []

for i in range(1,22):
    with open('Final_Data_of_Supplier{}.pkl'.format(i), 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        Loaded_Content.extend(content)




@app.post("/domainSearch")
async def getInformation(info : Request):
    print(await info.body())
    req_info = await info.json()
    CurrString = dict(req_info)["SearchedString"]
    Results = []

    f = open('Search-Data.json')

    data = json.load(f)


    return jsonable_encoder(data)


@app.post("/companySearch")
async def getInformation(info : Request):
    print(await info.body())
    req_info = await info.json()

    d = {
        "SupplierName": "Infosy",
         
        "Region": "APAC",
         
        "Country": "India",
         
        "Function": "IT & Infrastructure",
         
        "Service": "Applications Development",
         
        "AvgCost": "100k",
         
        "Rating": "90",
         
        "AverageDeliveryTime": "90",
         
        "NumberofEscalations": "5",
         
        "Year": "2018",
         
        "Resources": "10000"
         
        }

    return d






