from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot-data']

def get_db_data(location):
    print(location)
    if location.count:
        collection = db.place
        # info = 'It is a awesome place'
        # print(location)
        obj = collection.find_one(
            {'location': {"$regex": location[0], "$options":"i"}})
        if obj:
            info = obj['location'] + '\n' + obj['Description'] + '\n' + obj['Link']
        # print(obj)
    return info