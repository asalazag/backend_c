from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

        
@csrf_exempt
def CreateZPLCo(request): 
    request_data = request._body
    database = request_data['database'] 
    request_data = request._body
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #receive/createzplco?unido=24-162&tipodoc=C04&order=FE10204
        #Look for params
        tipodocto = request_data["tipodocto"] if "tipodocto" in request_data else None
        numdctoerp = request_data["numdctoerp"] if "numdctoerp" in request_data else None
        idempleado = request_data["idempleado"] if "idempleado" in request_data else None
        shwdata = request_data["shwdata"] if "shwdata" in request_data else None
        impresora_prt = request_data["impresora_prt"] if "impresora_prt" in request_data else None

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_recibociegoxdocto_zpl] %s, %s, %s, %s, %s'''

       #Try to execute
        try:
            response = exec_query(sp, (tipodocto,numdctoerp,idempleado,shwdata,impresora_prt,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)