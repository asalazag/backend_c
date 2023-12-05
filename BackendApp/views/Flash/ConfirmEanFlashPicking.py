from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from ...utils import *

@csrf_exempt
def ConfirmEanFlashPicking(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request._body 
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #customs/flash/confirmeanflashpicking?picking=#&ean=#&idempleado=#&
        #Look for params
        picking = request_data["picking"] if "picking" in request_data else None
        ean = request_data["ean"] if "ean" in request_data else None
        idempleado = request_data["idempleado"] if "idempleado" in request_data else None
      
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_confirmaEANdestelladoxpicking] %s,%s,%s'''

       #Try to execute
        try:
            response = exec_query(sp, (picking,ean,idempleado,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)