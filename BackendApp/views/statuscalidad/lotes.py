#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def lotes(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR LOS LOTES EN LISTA
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        Estado = request.GET["Estado"] if "Estado" in request.GET else ''
        fecha_inicio = request.GET["fecha_inicio"] if "fecha_inicio" in request.GET else ''
        fecha_fin = request.GET["fecha_fin"] if "fecha_fin" in request.GET else ''
        pedproveedor = request.GET["pedproveedor"] if "pedproveedor" in request.GET else ''
        
        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_getLotesEnLista_rct] %s, %s, %s, %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (bodega,Estado,fecha_inicio,fecha_fin,pedproveedor), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)

    # ACTUALIZAR EL ESTADO DE CALIDAD DE UN LOTE Y LE ASIGNA EL NUMERO DE CONTROL
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        Lote = request_data["Lote"] if "Lote" in request_data else ''
        ProductoEAN = request_data["ProductoEAN"] if "ProductoEAN" in request_data else ''
        Estado = request_data["Estado"] if "Estado" in request_data else ''
        Id_Usuario = request_data["Id_Usuario"] if "Id_Usuario" in request_data else 0
        NumControlLiberacion = request_data["NumControlLiberacion"] if "NumControlLiberacion" in request_data else ''

        response = []

        # print (request_data["permisosApp"])

        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_ActualizarStatusCalidadLote_rct] %s , %s , %s , %s , %s  '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (Lote, ProductoEAN, Estado, Id_Usuario, NumControlLiberacion,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)
