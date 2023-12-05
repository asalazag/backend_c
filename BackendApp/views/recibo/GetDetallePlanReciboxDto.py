from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

        
@csrf_exempt
def GetDetallePlanReciboxDto(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    # Get Inventory Close to Expiration
    if request.method == 'GET':
        #receive/getentrydocument?tipodoc=7-657&numdcto=FETX-702&idempleado=C08
        #Look for params
        
        #receive/entrydocument?tipodoc=C01&numdcto=2255
        #Look for params
        bodega = request.GET["bodega"] if "bodega" in request.GET else None
        tipodoc = request.GET["tipodoc"] if "tipodoc" in request.GET else None
        doctoErp = request.GET["doctoErp"] if "doctoErp" in request.GET else None

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_DetallePlanReciboxDto] %s, %s, %s'''

       #Try to execute

       #Try to execute
        try:
            response = exec_query(sp, (bodega,tipodoc,doctoErp,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)