import re
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from settings.models.config import config

from ...utils import *
from pymongo import MongoClient
from wmsAdapter.models import *


@csrf_exempt
def tables_fields(request):

    request_data = request._body
    #  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'GET':

        try:

            table = request.GET.get("table", None)
            plantilla = request.GET.get("plantilla", 0)
            idioma = request.GET.get("idioma", None)


            if table == None:
                return JsonResponse({"error": "No table provided"}, safe=False)

            table = table.lower()

            if table in (['euk', 'duk', 'art', 'epk', 'dpk', 'prv', 'clt', 'epn', 'dpn']):
                table = table[0].upper() + table[1:]
                table_name = eval(f'TdaWms{table}')
            elif table == 'history':
                table_name = eval('VTggTPicMultiproducto')
            elif table == 'seriales':
                table_name = eval('TdaWmsRelacionSerialesChild')
            else:
                return JsonResponse({"error": "Table not found"}, safe=False, status=400)

            print(table_name)

            fields = [field.name for field in table_name._meta.get_fields()]

            if int(plantilla) == 1:
                m = []
                for f in fields:
                    m.append({
                        "campo_origen": f,
                        "campo_destino": f,
                        "default": None,
                    })

                fields = m
            
            # Idioma
            if str(idioma).lower() == 'en':
                if table.lower() == 'art':
                    fields = ['sku','desctiption','reference','cost','group','subgroup','units per pack','weight','volume','provider code','unit price']
                elif table.lower() == 'clt' or table.lower() == 'prv':
                    fields = ['id','name','address','country code','currency','city','state','country','phone number','email','zip code']

            if str(idioma).lower() == 'es':
                if table.lower() == 'art':
                    fields = ['sku','descripcion','referencia','costo','grupo','subgrupo','unidad de empaque','peso','volumen ','codigo provedor','precio unidad','bodega']
                elif table.lower() == 'clt' or table.lower() == 'prv':
                    fields = ['id','name','address','country code','currency','city','state','country','phone number','email','zip code']

            # print(fields)

            return JsonResponse(fields, safe=False, status=200)

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
