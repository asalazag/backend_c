
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


        
@csrf_exempt
def GetProductsByPicking(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500)  
    # Get Inventory By Box
    if request.method == 'GET':
        #customs/orders/getlistordersorterbypicking?picking=#&
        #Look for params
        npedido = request.GET["npedido"] if "npedido" in request.GET else None
      
        
        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_obtenerDsArticulosxPicking] %s'''

       #Try to execute
        try:
            response = exec_query(sp, (npedido,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)