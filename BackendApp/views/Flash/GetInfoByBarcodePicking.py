
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


        
@csrf_exempt
def GetInfoByBarcodePicking(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500)  
    # Get Inventory By Box
    if request.method == 'GET':
        #customs/flash/getinfobybarcodepicking?picking=#&barcode=#&
        #Look for params
        picking = request.GET["picking"] if "picking" in request.GET else None
        barcode = request.GET["barcode"] if "barcode" in request.GET else None
      
        
        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_obtenerDSPickingDestelle] %s,%s'''

       #Try to execute
        try:
            response = exec_query(sp, (picking,barcode,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)