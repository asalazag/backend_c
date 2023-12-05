from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

@csrf_exempt
def AddBarcode(request): 

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
        idinternoean = request_data["idinternoean"] if "idinternoean" in request_data else None
        barcodeasignado = request_data["barcodeasignado"] if "barcodeasignado" in request_data else None
        qtyequivalente = request_data["qtyequivalente"] if "qtyequivalente" in request_data else None
        reemplazar = request_data["reemplazar"] if "reemplazar" in request_data else None
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spI_T_RelacionCodBarras_app] %s, %s, %s, %s'''

       #Try to execute
        try:
            response = exec_query(sp, (idinternoean,barcodeasignado,qtyequivalente,reemplazar,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)