
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def asignarlineaconteo(request):

    request_data = request._body
    database = request_data['database']

#  ASIGNA UNA CADENA DE LINEAS DE CONTEO A UN EMPLEADO INDICADO
    if request.method == 'PUT':

        idcadenalineas = request_data["idcadenalineas"] if "idcadenalineas" in request_data else ''
        idempleado = request_data["idempleado"] if "idempleado" in request_data else ''
        bod = request_data["bod"] if "bod" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_asigna_lineasConteoxIdEmpleado] %s , %s, %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (idcadenalineas, idempleado, bod,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
