import json
from pymongo import MongoClient
from settings.settings import *


def update_apikey(database:str, apikey:str):

    client = MongoClient(global_settings.CONNECTION_STRING)

    db = client['apiconfig']

    collection = db[database]

    item_details = collection.find({'apikey': {"$exists": True}})

    for item in item_details:
        item['apikey'] = apikey
        collection.update_one({'apikey': {"$exists": True}}, {"$set": item})
    
    client.close()


def update_token_quickbooks(database:str, RefreshToken:str, AccessToken:str):

    client = MongoClient(global_settings.CONNECTION_STRING)

    db = client['apiconfig']

    collection = db[database]

    item_details = collection.find({'quickbooks': {"$exists": True}})

    for item in item_details:
        item['quickbooks']['refreshToken'] = RefreshToken
        item['quickbooks']['qBData']['accessToken'] = AccessToken
        collection.update_one({'quickbooks': {"$exists": True}}, {"$set": item})
    
    client.close()



def update_token_sap_b1(database:str, token:str):

    client = MongoClient(global_settings.CONNECTION_STRING)

    db = client['apiconfig']

    collection = db[database]

    item_details = collection.find({'sap_b1': {"$exists": True}})

    for item in item_details:
        item['sap_b1']['SessionId'] = token
        collection.update_one({'sap_b1': {"$exists": True}}, {"$set": item})

    client.close()
        


