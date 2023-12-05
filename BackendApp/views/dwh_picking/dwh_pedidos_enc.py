from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *

@csrf_exempt
def dwh_pedidos_enc(request): 

    request_data = request._body
    database = request_data['database']


#  CONSULTAR LOS ENCABEZADO DE PEDIDO  QUE HACEN PARTE DE UN PICKING
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        pickingint = request.GET["pickingint"] if "pickingint" in request.GET else 0

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[dwh_pedidos_enc] %s'''


        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (pickingint,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
