from pymongo.mongo_client import MongoClient
import pickle

client = MongoClient("mongodb+srv://chethanreddy2002:12345@cluster0.xihwp.mongodb.net/?retryWrites=true&w=majority")
Data = client['Test']
MyData = Data['Test']



Loaded_Content = []

for i in range(1,22):
    with open('CostAddedData/Final_Data_of_Supplier{}.pkl'.format(i), 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        Loaded_Content.extend(content)


for data in Loaded_Content:
    MyData.insert_one(data)

print("All Data Inserted to Mongo Done!!!")

