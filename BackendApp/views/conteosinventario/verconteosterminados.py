from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def verconteosterminados(request):

    request_data = request._body
    database = request_data['database']
    idempleado = request_data['id_employee']
    warehouse = request_data['warehouse']

    # Ajusar conteo por linea
    if request.method == 'GET':
        
        if warehouse == "":
            warehouse = None      

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                    EXEC [web].[get_ConteosFinalizados] %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (warehouse,), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)


#  AJUSTE DE LOS RESULTADO DEL CONTEO TOTAL
    if request.method == 'PUT':

        conteo = request_data["conteo"] if "conteo" in request_data else 0
        idempleado = request_data["idempleado"] if "idempleado" in request_data else 0
        textoajuste = request_data["textoajuste"] if "textoajuste" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_ajusteDeCajasxvaloresDeIDConteo] %s , %s, %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (conteo, idempleado, textoajuste,), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
