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
def config_wms(request):

    request_data = request._body
    #  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'GET':

        try:

            table = request.GET.get("table", None)
            # print(table)

            c = config(request_data['database'], table)

            table_config = c.get_config()

            return JsonResponse([table_config], safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)

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
