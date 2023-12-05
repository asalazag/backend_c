import re
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from settings.models.config import config

from ...utils import *
from pymongo import MongoClient


@csrf_exempt
def databases_list(request):

    request_data = request._body

    database = request_data['database']
    print (database)
    #  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'GET':

        try:

            if database == 'dll':

                c = config(database, '')
                collections = c.get_collections()

                collections_list = []
                for collection in collections:
                    if collection != 'activities':
                        collections_list.append(collection)
                        print(collection)

                return JsonResponse(collections_list, safe=False, status=200)

            else:
                return JsonResponse({"message" : 'Invalid database'}, safe=False, status=500)

        except Exception as e:
            print(e)
            return JsonResponse({"message" : 'Server Error!'}, safe=False, status=500)

        else:
            print(e)
            return JsonResponse({"message" : 'Server Error!'}, safe=False, status=500)

    if request.method == 'POST':

        try:

            CONNECTION_STRING = "mongodb+srv://sgvsoftware:Sgv2019.@cluster0.7j0cuyj.mongodb.net/test"

            client = MongoClient(CONNECTION_STRING)

            db = client['copernicowms']

            collection = db[request_data['database']]

            request_data.pop("database")
            collection.insert_one(request_data)
            return JsonResponse({"success": "table configuration added"}, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)
