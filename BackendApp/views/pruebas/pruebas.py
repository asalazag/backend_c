from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def pruebas(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'POST':

        try:
            request_data.pop('database')
            request_data.pop('id_employee')
            request_data.pop('warehouse')
            request_data.pop('id_customer')
            request_data.pop('role')
            response = request_data
            return JsonResponse(response, safe=False, status=200)
            # response = exec_query(sp,Any=() ,database=database)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
