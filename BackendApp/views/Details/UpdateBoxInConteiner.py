from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from ...utils import *

@csrf_exempt
def UpdateBoxInConteiner(request): 

    try:
        database = request._body["database"] 
        print("Database: " + database)
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    # request_data = json.loads(request._body) 
    # print(request_data) 
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        print("UpdateBoxInConteiner")
        #customs/orders/updateboxinconteiner?pedido=#&unitarizador=#&tipoCaja=#&
        #Look for params
        pedido = str(request._body["pedido"]) if "pedido" in request._body else None
        unitarizador = str(request._body["unitarizador"]) if "unitarizador" in request._body else None
        tipoCaja = str(request._body["tipoCaja"]) if "tipoCaja" in request._body else None
      
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_actualizaTipoCajaEnContenedor] %s,%s,%s'''

       #Try to execute
        try:
            print("Executing SP: " + sp)
            print("Params: " + pedido + " " + unitarizador + " " + tipoCaja)
            response = exec_query(sp, (pedido,unitarizador,tipoCaja,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)