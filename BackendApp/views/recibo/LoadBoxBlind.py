from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

@csrf_exempt
def LoadBoxBliend(request): 
   
    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request.body
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #receive/loadboxblind
        #Look for params
        
        documentooc = request_data["documentooc"] if "documentooc" in request_data else None
        idempleado = request_data["idempleado"] if "idempleado" in request_data else None
        tipodocto = request_data["tipodocto"] if "tipodocto" in request_data else None

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_MDC_CargaInicial_From_ciego] %s, %s, %s'''

       #Try to execute
        try:
            response = exec_query(sp, (documentooc,idempleado,tipodocto,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)