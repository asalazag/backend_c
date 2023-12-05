#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from django.db import connections
from django.conf import settings
from ...utils import *
from settings.models.config import config
from pymongo import MongoClient
import re
@csrf_exempt
def equalize_validate_tables(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':

        origin = request_data["origin"] if "origin" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else None
        if origin is None:
            return JsonResponse({"message" : "origin is required"}, safe=False, status=405)
        elif destination is None:
            return JsonResponse({"message" : "destination is required"}, safe=False, status=405)
        try:
            list_table_base = []
            list_table_origin = []
            list_table_destination = []
            
            origen_cursor  = connections[origin].cursor()
            destination_cursor  = connections[destination].cursor()
            querysearch = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"

            origen_cursor.execute(querysearch)
            response = origen_cursor.fetchall()
            list_table_origin = [row[0] for row in response]
            #imprimir longitud de arreglo
            print(len(list_table_origin))
            # print(list_table_origin)
            destination_cursor.execute(querysearch)
            response = destination_cursor.fetchall()
            list_table_destination = [row[0] for row in response]
            print(len(list_table_destination))
            # print(list_table_destination)

            for table in list_table_origin:
                if table not in list_table_destination:
                    list_table_base.append(table)
            print(len(list_table_base))
            print (list_table_base)
            if len(list_table_base) > 0:
                return JsonResponse({"Tablas" : list_table_base}, safe=False, status=200)
            else:
                return JsonResponse({"message" : "No hay tablas que crear"}, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"message" : str(e)}, safe=False,status=500)

