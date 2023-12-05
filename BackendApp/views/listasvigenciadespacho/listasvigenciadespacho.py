from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def listasvigenciadespacho(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[sps_t_detalle_referencia_CD_rct] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (bodega,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)


# ADICIONA UN REGISTRO DE ZONAS POR EMPLEADO
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else ''
        codigoreferencia = request_data["codigoreferencia"] if "codigoreferencia" in request_data else ''
        listavigencias = request_data["listavigencias"] if "listavigencias" in request_data else ''
        diasvigenciacliente = request_data["diasvigenciacliente"] if "diasvigenciacliente" in request_data else ''
        diasvigenciamin = request_data["diasvigenciamin"] if "diasvigenciamin" in request_data else ''
        bodega = request_data["bodega"] if "bodega" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spi_t_detalle_referencia_CD_rct] %s , %s , %s ,%s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (productoEAN, codigoreferencia, listavigencias,
                                  diasvigenciacliente, diasvigenciamin, bodega), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)


# ACTUALIZAR UN CAMPO DE ZONAS POR EMPLEADO
    if request.method == 'PUT':

       # id = request.GET["id"] if "id" in request.GET else ''
        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else ''
        codigoreferencia = request_data["codigoreferencia"] if "codigoreferencia" in request_data else ''
        listavigencias = request_data["listavigencias"] if "listavigencias" in request_data else ''
        diasvigenciacliente = request_data["diasvigenciacliente"] if "diasvigenciacliente" in request_data else ''
        diasvigenciamin = request_data["diasvigenciamin"] if "diasvigenciamin" in request_data else ''
        bodega = request_data["bodega"] if "bodega" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spu_t_detalle_referencia_CD_rct] %s , %s , %s , %s , %s , %s '''

        # print (sp)
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (productoEAN, codigoreferencia, listavigencias,
                                  diasvigenciacliente, diasvigenciamin, bodega), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)


# ACTUALIZAR UN CAMPO DE DESCRIPCIONES
    if request.method == 'DELETE':

        # print (request.method);

        # id = request.GET["id"] if "id" in request.GET else ''
        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else ''
        listavigencias = request_data["listavigencias"] if "listavigencias" in request_data else ''
        bodega = request_data["bodega"] if "bodega" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spD_t_detalle_referencia_CD_rct] %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(
                sp, (productoEAN, listavigencias, bodega), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
