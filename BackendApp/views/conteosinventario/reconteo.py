from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def reconteo(request):

    request_data = request._body
    database = request_data['database']


# PROGRAMAR UN CONTEO
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        idConteo = request_data["idConteo"] if "idConteo" in request_data else 0
        realiza = request_data["realiza"] if "realiza" in request_data else ''
        idempleado = request_data["idempleado"] if "idempleado" in request_data else 0
        idConteoBase = request_data["idConteoBase"] if "idConteoBase" in request_data else 0

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_recarga_T_Temporar_Encabezado_Conteo] %s , %s , %s, %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(
                sp, (idConteo, realiza, idempleado, idConteoBase,), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)


# OBTENER UN GRUPO DE FILTRO GENERICO POR ZONAS, PASILLOS, MUEBLES ETC
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        objetofn = request.GET["objetofn"] if "objetofn" in request.GET else ''
        cadenaparameros = request.GET["cadenaparameros"] if "cadenaparameros" in request.GET else ''
        bod = request.GET["bod"] if "bod" in request.GET else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_obtenerlistaxobjetofninvxbodega] %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (objetofn, cadenaparameros, bod), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)
