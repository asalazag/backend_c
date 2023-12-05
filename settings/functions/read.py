from pymongo import MongoClient
from settings.settings import *

def get_collections():

    client = MongoClient(global_settings.CONNECTION_STRING)

    db = client['apiconfig']

    collections = db.list_collection_names()

    return collections


def get_apikeys() -> dict:


    client = MongoClient(global_settings.CONNECTION_STRING)

    db = client['apiconfig']

    apikeys = {}

    for collection in db.list_collection_names():
        collection = db[collection]
        item_details = collection.find({'apikey': {"$exists": True}})
        for item in item_details:
            apikeys[item['apikey']] = collection.name
    
    client.close()

    return apikeys

def get_db_connection() -> dict:

    client = MongoClient(global_settings.CONNECTION_STRING)

    db = client['apiconfig']

    db_connection = {}

    for collection in db.list_collection_names():
        collection = db[collection]
        item_details = collection.find({'wms': {"$exists": True}})
        for item in item_details:
            db_connection[collection.name] = item['wms']['db']

    client.close()

    return db_connection
