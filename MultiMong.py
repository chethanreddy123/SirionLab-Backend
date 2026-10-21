import os
from pymongo.mongo_client import MongoClient
import pickle

C1 = MongoClient(os.environ["MONGODB_URI_2"])
myData1 = C1['Test']['Test']

C2 = MongoClient(os.environ["MONGODB_URI_3"])
myData2 = C2['Test']['Test']

C3 = MongoClient(os.environ["MONGODB_URI_4"])
myData3 = C3['Test']['Test']

C4 = MongoClient(os.environ["MONGODB_URI_5"])
myData4 = C4['test']['test']

List_Of_Clusters = [C1, C2, C3, C4]


for i in range(1,6):
    with open('CostAddedData/Final_Data_of_Supplier{}.pkl'.format(i), 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        myData1.insert_many(content)



for i in range(6,11):
    with open('CostAddedData/Final_Data_of_Supplier{}.pkl'.format(i), 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        myData2.insert_many(content)

for i in range(11,16):
    with open('CostAddedData/Final_Data_of_Supplier{}.pkl'.format(i), 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        myData3.insert_many(content)

for i in range(16,22):
    with open('CostAddedData/Final_Data_of_Supplier{}.pkl'.format(i), 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        myData4.insert_many(content)

