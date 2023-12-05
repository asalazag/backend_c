from pymongo import MongoClient
from settings.settings import *


class config:

    def __init__(self, database: str, obj: str):
        self.CONNECTION_STRING = global_settings.CONNECTION_STRING
        self.client = MongoClient(self.CONNECTION_STRING)
        self.db = self.client['copernicowms']
        self.collections = self.db.list_collection_names()
        self.database = database
        self.obj = obj

    def get_collections(self):
        return self.collections

    def get_config(self):
        collection = self.db[self.database]
        json_query = {self.obj: {"$exists": True}}
        item_details = collection.find(json_query)
        config = []
        for item in item_details:
            item.pop('_id')
            config.append(item)
        return config[0]
