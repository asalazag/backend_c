from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def regsanitario(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAMOS LOS REGISTROS SANITAROS CORRESPONDIENTES A LA REFERENCIA INDICADA
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        ean = request.GET["ean"] if "ean" in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_obtenerRegistroSanitarioxEan] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (ean,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)


# ADICIONA EL REGISTRO SANITARIO
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        Cod_Registro = request_data["Cod_Registro"] if "Cod_Registro" in request_data else ''
        ProductoEAN = request_data["ProductoEAN"] if "ProductoEAN" in request_data else ''
        FechaRegistro = request_data["FechaRegistro"] if "FechaRegistro" in request_data else ''
        FechaVencimiento = request_data["FechaVencimiento"] if "FechaVencimiento" in request_data else ''
        CodPaisRegistro = request_data["CodPaisRegistro"] if "CodPaisRegistro" in request_data else ''
        Estado = request_data["Estado"] if "Estado" in request_data else 0

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spWMS_Insertar_Registo_Sanitario] %s , %s , %s ,%s , %s, %s   '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (Cod_Registro, ProductoEAN, FechaRegistro, FechaVencimiento, CodPaisRegistro, Estado,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)


# ACTUALIZAR LA INFORMACION DE UN REGISTRO SANITARIO
    if request.method == 'PUT':

        id = request_data["id"] if "id" in request_data else 0
        Cod_Registro = request_data["Cod_Registro"] if "Cod_Registro" in request_data else ''
        ProductoEAN = request_data["ProductoEAN"] if "ProductoEAN" in request_data else ''
        FechaRegistro = request_data["FechaRegistro"] if "FechaRegistro" in request_data else ''
        FechaVencimiento = request_data["FechaVencimiento"] if "FechaVencimiento" in request_data else ''
        CodPaisRegistro = request_data["CodPaisRegistro"] if "CodPaisRegistro" in request_data else ''
        Estado = request_data["Estado"] if "Estado" in request_data else 0

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spWMS_Actualizar_Registo_Sanitario]  %s , %s , %s ,%s , %s, %s , %s '''
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (id, Cod_Registro, ProductoEAN, FechaRegistro, FechaVencimiento, CodPaisRegistro, Estado,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)


# ELIMINA UN ID DE REGISTRO SANITARIO
    if request.method == 'DELETE':

        # print (request.method);

        id = request.GET["id"] if "id" in request.GET else ''
        
        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spWMS_Eliminar_Registo_Sanitario] %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (id,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)
