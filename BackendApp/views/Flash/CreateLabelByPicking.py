from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from ...utils import *

@csrf_exempt
def CreateLabelByPicking(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request._body 
    # Get Inventory Close to Expiration
    if request.method == 'PUT':
        #customs/flash/createlabelbypicking?picking=#&idempleado=#&shwdata=#&impresora=#&
        #Look for params
        picking = request_data["picking"] if "picking" in request_data else None
        idempleado = request_data["idempleado"] if "idempleado" in request_data else None
        shwdata = request_data["shwdata"] if "shwdata" in request_data else None
        impresora = request_data["impresora"] if "impresora" in request_data else None
      
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_ssccxcaja_ZPL_destelle] %s,%s,%s,%s'''

       #Try to execute
        try:
            response = exec_query(sp, (picking,idempleado,shwdata,impresora,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)