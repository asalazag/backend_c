#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def obtenerdatosguia(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTA LOS NUMEROS DE PICKING DISPONIBLES PARA GENERAR UNA GUIA DE TRANSPORTE
    if request.method == 'GET':

        picking = request.GET['picking'] if 'picking' in request.GET else None
        bigpedido = request.GET['bigpedido'] if 'bigpedido' in request.GET else None

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[awg_obtenerDataparaGuiaTte] %s , %s  '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (picking, bigpedido), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)


# GENERA LA GUIA Y ACTUALIZA EL DATO EN LA TABLA TDA_WMS_TTE
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        picking     = request_data["picking"]   if "picking"    in request_data else 0
        bigpedido   = request_data["bigpedido"] if "bigpedido"  in request_data else ''
        numguia     = request_data["numguia"]   if "numguia"    in request_data else ''

        response = []

        # print (request_data["permisosApp"])

        sp = '''SET NOCOUNT ON
                EXEC [web].[spu_tda_wms_tte_guia] %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (picking, bigpedido,numguia ), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
