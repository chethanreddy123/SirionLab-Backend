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
    with open('CostAddedData/Final_Data_of_Supplier{}.pkl'.format(i), 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        Loaded_Content.extend(content)




@app.post("/domainSearch")
async def getInformation(info : Request):
    # print(await info.body())
    req_info = await info.json()
    CurrString = dict(req_info)["SearchedString"]
    Results = []
    # print(Loaded_Content[0])

    for i in Loaded_Content:
        if len(Results) == 3:
            break
        if i['Function'] == CurrString:
            Results.append(i)

    Final_Data = {"List" : Results}
    return Final_Data


@app.post("/companySearch")
async def getInformation(info : Request):
    print(await info.body())
    req_info = await info.json()
    CurrString = dict(req_info)["SearchedString"]
    Results = []

    for i in Loaded_Content:
        if i['SupplierName'] == CurrString:
            Results.append(i)
            break

    return Results[0]

@app.post("/predictionSearch")
async def getInformation(info : Request):
    print(await info.body())
    req_info = await info.json()
    CurrString = dict(req_info)["SearchedString"]
    Results = []






