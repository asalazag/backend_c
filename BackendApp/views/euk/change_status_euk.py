
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


        
@csrf_exempt
def change_estatus_euk(request): 

    try:
        request_data = request._body
        database = request_data['database'] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500)  
    # Get Inventory By Box
    if request.method == 'POST':
        #customs/orders/getpickingbyorder?npedido=#&eandecaja=#&
        #Look for params
        tipodocto = request_data["tipodocto"] if "tipodocto" in request_data else None
        doctoerp = request_data["doctoerp"] if "doctoerp" in request_data else None
        numdocumento = request_data["numdocumento"] if "numdocumento" in request_data else None
        
        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_changeStatusEuk] %s,%s,%s'''

       #Try to execute
        try:
            response = exec_query(sp, (tipodocto,doctoerp,numdocumento,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)