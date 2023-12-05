import re
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BackendApp.functions.mongo.plantillas.get_plantillas import get_plantillas
from settings.models.config import config

from pymongo import MongoClient


@csrf_exempt
def plantillas(request):

    request_data = request._body
    #  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'GET':

        try:

            table = request.GET.get("table", None)

            print(table)
            print("-------------------------------")

            if table:
                table = table.split('-')
                print(table)
            else:
                return JsonResponse({'Error': 'Does not exist'}, safe=False, status=404)

            table_config = get_plantillas(
                request_data['database'], table[0], None)

            plantillas_keys = []
            for t in table_config:
                plantillas_keys.extend(list(t.keys()))

            # plantillas_keys = list(set(plantillas_keys))

            return JsonResponse(plantillas_keys, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)

    # if request.method == 'POST':

    #     try:

    #         CONNECTION_STRING = "mongodb+srv://sgvsoftware:Sgv2019.@cluster0.7j0cuyj.mongodb.net/test"

    #         client = MongoClient(CONNECTION_STRING)

    #         db = client['copernicowms']

    #         collection = db[request_data['database']]

    #         request_data.pop("database")
    #         collection.insert_one(request_data)
    #         return JsonResponse({"success": "table configuration added"}, safe=False, status=200)

    #     except Exception as e:
    #         print(e)
    #         return JsonResponse('Server Error!', safe=False, status=500)
