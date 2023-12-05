from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests

from BackendApp.functions.api.apikey import get_apikey

from ...utils import *


@csrf_exempt
def api(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'GET':
        try:

            table = request.GET["table"] if "table" in request.GET else ''
            print(table)

            if database == 'default':
                database = 'desarrollo'
            apikey = requests.get(
                f'https://api.copernicowms.com/wms/get-apikey?database={database}').json()['apikey']

            headers = {
                'Authorization': apikey
            }

            response = requests.get(
                f'https://api.copernicowms.com/wms/{table}', headers=headers).json()

            return JsonResponse(response, safe=False, status=200)
            # response = exec_query(sp,Any=() ,database=database)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
        

    if request.method == 'POST':
        try:

            if database == 'default':
                database = 'desarrollo'
            
            apikey = get_apikey(database)

            return JsonResponse(apikey, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
