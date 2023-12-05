from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *
        
@csrf_exempt
def articles(request): 

    request_data = request._body
    database = request_data['database']

#  CONSULTAR TODOS LOS ARTICUULOS DE UNA BODEGA O POR EAN O POR COMBINACION DE BODEGA Y EAN
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        productoEAN = request.GET["productoEAN"] if "productoEAN" in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[sps_v_wms_articulos_rct] %s , %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (bodega,productoEAN), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
