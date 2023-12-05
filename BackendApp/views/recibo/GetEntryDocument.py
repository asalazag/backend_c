from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

        
@csrf_exempt
def GetEntryDocuments(request): 

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
        tipodoc = request.GET["tipodoc"] if "tipodoc" in request.GET else None
        numdcto = request.GET["numdcto"] if "numdcto" in request.GET else None

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_documentosEntrada] %s, %s'''

       #Try to execute

       #Try to execute
        try:
            response = exec_query(sp, (tipodoc,numdcto,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)