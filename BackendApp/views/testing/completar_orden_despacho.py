
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BackendApp.tests.TdaWmsDpk.completar_lineas import completar_lineas_TdaWmsDpk

from ...utils import *


        
@csrf_exempt
def completar_orden_despacho(request): 

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
            numpedido = request.GET['numpedido'] if 'numpedido' in request.GET else None

            if numpedido is None:   
                numpedido = doctoerp

            if db is None: 
                db = database

            response = completar_lineas_TdaWmsDpk(doctoerp=doctoerp, tipodocto=tipodocto, numpedido=numpedido, database=db)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse(str(e), safe=False, status=500)