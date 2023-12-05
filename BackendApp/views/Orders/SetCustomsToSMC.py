from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from ...utils import *

@csrf_exempt
def SetCustomsToSMC(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request._body 
    # Get Inventory Close to Expiration
    if request.method == 'PUT':
        #customs/orders/setcustomstosmc?bigpicking=#&
        #Look for params
        bigpicking = request_data["bigpicking"] if "bigpicking" in request_data else None
      
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_sendAduanaToSMC]  %s'''

       #Try to execute
        try:
            response = exec_query(sp, (bigpicking,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)