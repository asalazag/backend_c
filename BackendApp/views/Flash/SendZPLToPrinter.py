from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from ...utils import *

@csrf_exempt
def SendZPLToPrinter(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request._body 
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #customs/flash/sendzpltoprinter?idusuario=#&codigo_dinamica=#&ord_no=#&impresora=#&
        #Look for params
        idusuario = request_data["idusuario"] if "idusuario" in request_data else None
        codigo_dinamica = request_data["codigo_dinamica"] if "codigo_dinamica" in request_data else None
        ord_no = request_data["ord_no"] if "ord_no" in request_data else None
        impresora = request_data["impresora"] if "impresora" in request_data else None
      
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [cmn].[generarTxtImpresionCajas] %s,%s,%s,%s'''

       #Try to execute
        try:
            response = exec_query(sp, (idusuario,codigo_dinamica,ord_no,impresora,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)