import pymongo
from pymongo import MongoClient


# client = MongoClient("localhost", 27017)
# db = client['test']
# print(client.list_database_names())
# collection = db['user']
# doc1 = {"name": "Test User1", "age": "26", "city": "Banglore"}
# doc2 = {"name": "Test User2", "age": "26", "city": "Banglore"}
# doc3 = {"name": "Test User3", "age": "26", "city": "Banglore"}
# collection.insert_one(doc1)
# collection.insert_many([doc2, doc3])
# a = collection.upda
# import pdb; pdb.set_trace()

class MongoDataManager:
    def __init__(self, db_name, collection_name) -> None:
        self.client = MongoClient("localhost", 27017)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def insert_document(self, data):
        """
        Add data to collection.
        Input:
            data -> Either single data as dict or multiple data as a list of dict.
        """
        try:
            if type(data) == dict:
                return self.collection.insert_one(data).acknowledged
            elif type(data) == list:
                return self.collection.insert_many(data).acknowledged
        except (TypeError, pymongo.errors.DuplicateKeyError):
            return False
    
    def find_unique_document(self, unique_field, value):
        return self.collection.find_one({unique_field: value})
    
    def find_all_documents(self):
        return [doc for doc in self.collection.find()]
    
    def search_document(self, field, value):
        return [doc for doc in self.collection.find({field: value})]
    
    def update_single_document(self, id, field, value):
        self.collections.update_one({'_id': id}, {'$set': {field: value}})
    
    def delete_multiple_documents(self, field, value):
        self.collection.delete_many({field: value})
    
    def delete_single_document(self, unique_field, value):
        self.collection.delete_one({unique_field: value})
    
    
    # def delete_single_document(self, )
    
