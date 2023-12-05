from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

        
@csrf_exempt
def EndReceive(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request.body
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #receive/endreceive?unido=24-162&tipodoc=C04&order=FE10204
        #Look for params
        unido = request_data["unido"] if "unido" in request_data else None
        tipodoc = request_data["tipodoc"] if "tipodoc" in request_data else None
        order = request_data["order"] if "order" in request_data else None

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_descuentaLineasConIgualCodigo_DUK] %s, %s, %s'''

       #Try to execute
        try:
            response = exec_query(sp, (unido,tipodoc,order,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)