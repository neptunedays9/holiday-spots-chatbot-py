from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot-data']

def GetInfo(location):
    print(location)
    if location.count:
        collection = db.place
        # info = 'It is a awesome place'
        print(location)
        obj = collection.find_one({'location':location[0]})
        print(obj)
    return obj['info']