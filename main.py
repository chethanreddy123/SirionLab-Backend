from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
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


from pymongo.mongo_client import MongoClient
import pickle

C1 = MongoClient('mongodb+srv://chethanreddy2002:12345@cluster0.xihwp.mongodb.net/?retryWrites=true&w=majority')
myData1 = C1['Test']['Test']

C2 = MongoClient('mongodb+srv://chethan1234:12345@cluster0.6ouanj6.mongodb.net/?retryWrites=true&w=majority')
myData2 = C2['Test']['Test']

C3 = MongoClient('mongodb+srv://chethan1234:12345@cluster0.uou14qn.mongodb.net/?retryWrites=true&w=majority')
myData3 = C3['Test']['Test']

C4 = MongoClient('mongodb+srv://achethanreddy1921:12345@cluster0.pcjvpav.mongodb.net/?retryWrites=true&w=majority')
myData4 = C4['test']['test']

List_Of_Clusters = [myData1, myData2, myData3, myData4]




@app.post("/domainSearch")
async def getInformation(info : Request):
    # print(await info.body())
    req_info = await info.json()
    CurrString = dict(req_info)["SearchedString"]
    Results = []
    def get_data(n):
        for i in List_Of_Clusters[n].find({"Function" : CurrString}):
            yield(i)



    for i in range(4):
        if len(Results) >= 3:
            break
        cuList = get_data(i)
        while True:
            try:
 
            # Iterate by calling next
                item = next(cuList)
                del item['_id']
                Results.append(item)
                if len(Results) == 3:
                    break
            except StopIteration:
 
                # exception will happen when iteration will over
                break


    Final_Data = {"List" : Results}
    return Final_Data


@app.post("/companySearch")
async def getInformation(info : Request):
    print(await info.body())
    req_info = await info.json()
    CurrString = dict(req_info)["SearchedString"]
    Results = []

    print(List_Of_Clusters[0].find({"SupplierName" : CurrString}))

    def get_data(n):
        for i in List_Of_Clusters[n].find({"SupplierName" : CurrString}):
            yield(i)


    check = False

    for i in range(4):

        cuList = get_data(i)
        if check == True:
            break
        while True:
            try:

                item = next(cuList)
                del item['_id']
                Results.append(item)
                check = True
                break
                
            except StopIteration:
 
                # exception will happen when iteration will over
                break

    return Results[0]

@app.post("/predictionSearch")
async def getInformation(info : Request):
    print(await info.body())
    req_info = await info.json()
    CurrString = dict(req_info)["SearchedString"]
    Results = []






