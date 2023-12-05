from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

@csrf_exempt
def genera_rotulo_zpl(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request._body 
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #receive/addblindbatch
        #Look for params
        picking = request_data["picking"] if "picking" in request_data else None
        idempleado = request_data["idempleado"] if "idempleado" in request_data else None
        impresora = request_data["impresora"] if "impresora" in request_data else None
        numpedido = request_data["numpedido"] if "numpedido" in request_data else None
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_genera_rotulo_tranportadora_coordinadora] %s, %s, %s, %s'''

       #Try to execute
        try:
            response = exec_query(sp, (picking,idempleado,impresora,numpedido,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)