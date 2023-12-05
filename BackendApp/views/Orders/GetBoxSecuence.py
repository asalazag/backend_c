
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


        
@csrf_exempt
def GetBoxSecuence(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500)  
    # Get Box number
    if request.method == 'GET':
      
        
        #Sp to exec
        sp = ''' select next value for [dbo].[secuencia_unitarizador] '''

       #Try to execute
        try:
            response = exec_query(sp, (), database=database)
            response = response[0] if len(response) > 0 else None
            if response is None:
                return JsonResponse(response, safe=False, status=400)
            else:
                final_response = {
                    "box" : response[""]
                }
                return JsonResponse(final_response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)