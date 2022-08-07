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

