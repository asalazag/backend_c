from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

@csrf_exempt
def GetInfoByArticle(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    # Get Inventory Close to Expiration
    if request.method == 'GET':
        #receive/getinfobyeanoc?barcode=12&oc=9169-7852&tipodoc=MPT
        #Look for params
        ean = request.GET["ean"] if "ean" in request.GET else None
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_obtenerDsInfoxWMS_Articulo] %s'''

       #Try to execute
        try:
            response = exec_query(sp, (ean,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)