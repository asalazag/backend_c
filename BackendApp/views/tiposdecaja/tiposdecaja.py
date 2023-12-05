from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def tiposdecaja(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAMOS LOS TIPOS DE CAJA
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        # bodega = request_data["bodega"] if "bodega" in request_data else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spS_TiposDeCaja] '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)


# ADICIONA UN TIPO DE CAJA
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        tipo_caja = request_data["tipo_caja"] if "tipo_caja" in request_data else None
        descripcion_caja = request_data["descripcion_caja"] if "descripcion_caja" in request_data else None
        peso = request_data["peso"] if "peso" in request_data else None
        alto = request_data["alto"] if "alto" in request_data else None
        ancho = request_data["ancho"] if "ancho" in request_data else None
        largo = request_data["largo"] if "largo" in request_data else None
        volumen = request_data["volumen"] if "volumen" in request_data else None
        factor = request_data["factor"] if "factor" in request_data else None

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spI_TiposDeCaja] %s , %s , %s ,%s , %s, %s , %s , %s  '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (tipo_caja, descripcion_caja, peso, alto, ancho, largo, volumen, factor), database=database)

            # Returns the response
            # Conversion de la respuesta al formato que recibe el front
            if len(response) > 0:
                print("The length of the response is " + str(len(response)))
                return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)


# ACTUALIZAR UN CAMPO DE ZONAS POR EMPLEADO
    if request.method == 'PUT':

        tipo_caja = request_data["tipo_caja"] if "tipo_caja" in request_data else ''
        descripcion_caja = request_data["descripcion_caja"] if "descripcion_caja" in request_data else 0
        peso = request_data["peso"] if "peso" in request_data else 0
        alto = request_data["alto"] if "alto" in request_data else 0
        ancho = request_data["ancho"] if "ancho" in request_data else 0
        largo = request_data["largo"] if "largo" in request_data else 0
        volumen = request_data["volumen"] if "volumen" in request_data else 0
        factor = request_data["factor"] if "factor" in request_data else 0

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spU_TiposDeCaja]  %s , %s , %s ,%s , %s, %s , %s , %s  '''
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (tipo_caja, descripcion_caja, peso, alto, ancho, largo, volumen, factor), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)

        # Conversion de la respuesta al formato que recibe el front


# ACTUALIZAR UN CAMPO DE DESCRIPCIONES
    if request.method == 'DELETE':

        tipo_caja = request_data["tipo_caja"] if "tipo_caja" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spD_TiposDeCaja] %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (tipo_caja,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)
