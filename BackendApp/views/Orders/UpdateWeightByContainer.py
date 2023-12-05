from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from ...utils import *

@csrf_exempt
def UpdateWeightByContainer(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request._body 
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #customs/orders/updateweightbycontainer?NUMPEDIDO=#&contenedor=#&peso=#&
        #Look for params
        NUMPEDIDO = request_data["NUMPEDIDO"] if "NUMPEDIDO" in request_data else None
        contenedor = request_data["contenedor"] if "contenedor" in request_data else None
        peso = request_data["peso"] if "peso" in request_data else None
      
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_registraPesoxIdContenedorPicking] %s,%s,%s'''

       #Try to execute
        try:
            response = exec_query(sp, (NUMPEDIDO,contenedor,peso,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)