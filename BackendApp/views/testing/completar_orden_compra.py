
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BackendApp.tests.TdaWmsDuk.completar_lineas import completar_lineas_TdaWmsDuk

from ...utils import *


        
@csrf_exempt
def completar_orden_compra(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500)  

    if request.method == 'GET':

        print("GET")
      
        try:
            db = request.GET['database'] if 'database' in request.GET else None
            tipodocto = request.GET['tipodocto'] if 'tipodocto' in request.GET else None
            doctoerp = request.GET['doctoerp'] if 'doctoerp' in request.GET else None
            numdocumento = request.GET['numdocumento'] if 'numdocumento' in request.GET else None

            if numdocumento is None:   
                numdocumento = doctoerp

            if db is None: 
                db = database

            try:
                # response = []
                sp = ''' SET NOCOUNT ON
                    EXEC [dbo].[usp_multiproductoInConFacturaDuk] %s, %s, %s, %s'''
                
                response = exec_query(sp, (tipodocto,doctoerp,numdocumento, request._body["id_employee"] ), database=database)
                print(response)
            
            except Exception as e:
                print("Something went wrong ", e)

            response = completar_lineas_TdaWmsDuk(doctoerp=doctoerp, tipodocto=tipodocto, numdocumento=numdocumento, database=db)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse(str(e), safe=False, status=500)