from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def conteo(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UN CONTEO POR SU ID (WMS-45)
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        idConteo = request.GET["idConteo"] if "idConteo" in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_ObtenerResultadoxIDConteo] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (idConteo,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)



# PROGRAMAR UN CONTEO
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        bod = request_data["bod"] if "bod" in request_data else ''
        eanes = request_data["eanes"] if "eanes" in request_data else ''
        referencias = request_data["referencias"] if "referencias" in request_data else ''
        zonas = request_data["zonas"] if "zonas" in request_data else ''
        priorioridadrotacion = request_data["priorioridadrotacion"] if "priorioridadrotacion" in request_data else ''
        ubicaciones = request_data["ubicaciones"] if "ubicaciones" in request_data else ''

        pisos = request_data["pisos"] if "pisos" in request_data else ''
        Id_empleado = request_data["Id_empleado"] if "Id_empleado" in request_data else ''
        generaconteo = request_data["generaconteo"] if "generaconteo" in request_data else ''
        fila_piso = request_data["fila_piso"] if "fila_piso" in request_data else ''
        modulos = request_data["modulos"] if "modulos" in request_data else ''
        grupos = request_data["grupos"] if "grupos" in request_data else ''
        subgrupos = request_data["subgrupos"] if "subgrupos" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[sp_ObtienedatosparaConteo_ext] %s , %s , %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s '''

        # Query que se hace directamente a la base de datos
        try:
            
            response = exec_query(sp,
                                  (bod, eanes, referencias, zonas, priorioridadrotacion, ubicaciones,
                                   pisos, Id_empleado, generaconteo, fila_piso, modulos, grupos, subgrupos),
                                  database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

# UNIFICAR UN CONTEO SECUNDARIO EN CONTEO BASE
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        idConteoBase = request_data["idConteoBase"] if "idConteoBase" in request_data else 0
        idReconteo = request_data["idReconteo"] if "idReconteo" in request_data else 0

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_ActualizaReconteoEnConteoBase] %s , %s  '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (idConteoBase, idReconteo,), database=database)
            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)

# ELIMINAR UN ID DE CONTEO DE TODAS LAS TABLAS QUE SE VINCULAN
    if request.method == 'DELETE':

        # id = request.GET["id"] if "id" in request.GET else ''
        idConteo = request_data["idConteo"] if "idConteo" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spD_T_Temporar_Encabezado_ConteoWMS_Customized] %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (idConteo,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)