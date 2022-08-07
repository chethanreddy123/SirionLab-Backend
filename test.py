from pymongo.mongo_client import MongoClient

C1 = MongoClient('mongodb+srv://chethan1234:12345@cluster0.6ouanj6.mongodb.net/?retryWrites=true&w=majority')

C2 = MongoClient('mongodb+srv://chethan1234:12345@cluster0.uou14qn.mongodb.net/?retryWrites=true&w=majority')

C3 = MongoClient('mongodb+srv://achethanreddy1921:12345@cluster0.pcjvpav.mongodb.net/?retryWrites=true&w=majority')

myData = C3['test']['test']
print(list(myData.find({"Function" : "Software"})))