import json
from pymongo import MongoClient
from settings.settings import *

def post_new_collection(database:str):
    CONNECTION_STRING = global_settings.CONNECTION_STRING

    client = MongoClient(CONNECTION_STRING)

    db = client['apiconfig']

    with open('settings/functions/default.json') as default_config:
        registers = json.load(default_config)

    collection = db[database]
    
    for i in registers:
        print({i : registers[i]})
        db[database].insert_one({i : registers[i]})

    client.close()

    # collection.insert_one(request_data)