#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def copiarguia(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTA DE LOS CODIGOS DISPONIBLES DE CIUDADES DANE
    if request.method == 'GET':

        bodega = request.GET['bodega'] if 'bodega' in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_obtenerTransportadoraconvenio] %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (bodega,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)

        # Conversion de la respuesta al formato que recibe el front
# AGREGA LAS TABLAS DE ENCABEZADO Y DETALLE DE TRANSPORTE CON BASE EN LOS DATOS ENVIADOS
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        picking = request_data["picking"] if "picking" in request_data else ''
        bignumpedido = request_data["bignumpedido"] if "bignumpedido" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spi_tda_wms_tte] %s , %s  '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (picking, bignumpedido), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

# ACTUALIZAR LOS DATOS CORRESPONDIENTS A UNA GUIA DE ENVIO CON BASE EN  LA DATA DEL FORMULARIO ENVIADO
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        picking = int(request_data["picking"]) if "picking" in request_data else 0
        codigo_convenio = request_data["codigo_convenio"] if "codigo_convenio" in request_data else None
        bigpedido = request_data["bigpedido"] if "bigpedido" in request_data else ''
        cod_ciudadDestino = request_data["cod_ciudadDestino"] if "cod_ciudadDestino" in request_data else ''
        numFactura = request_data["numFactura"] if "numFactura" in request_data else ''
        vl_declarado = int(float(request_data["vl_declarado"])) if "vl_declarado" in request_data else 0
        qtyCajas = int(request_data["qtyCajas"]) if "qtyCajas" in request_data else 0
        totalPeso = int(float(request_data["totalPeso"])) if "totalPeso" in request_data else 0
        transportadora = request_data["transportadora"] if "transportadora" in request_data else None

        response = []

        # print (request_data["permisosApp"])

        sp = '''SET NOCOUNT ON
                EXEC [web].[spu_tda_wms_tte] %s , %s , %s, %s , %s , %s, %s , %s, %s  '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (picking, codigo_convenio, bigpedido, cod_ciudadDestino, numFactura, vl_declarado, qtyCajas, totalPeso, transportadora), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
