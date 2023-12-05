from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from ...utils import *

@csrf_exempt
def FinishCustomsByOrder(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request._body 
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #customs/orders/finishcustomsbyorder?pedido=#&
        #Look for params
        pedido = request_data["pedido"] if "pedido" in request_data else None
      
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_TerminarAduanaDePicking_AduanaNew_app_pedido] %s'''

       #Try to execute
        try:
            response = exec_query(sp, (pedido,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Items not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)