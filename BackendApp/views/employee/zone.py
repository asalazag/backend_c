from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def zone(request):

    request_data = request._body
    database = request_data['database']
#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        corporacion = request_data["corporacion"] if "corporacion" in request_data else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spS_T_ins_Zona_Empleado_rct] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (corporacion,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)


# ADICIONA UN REGISTRO DE ZONAS POR EMPLEADO
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        idusuario = request_data["idusuario"] if "idusuario" in request_data else ''
        Zona = request_data["Zona"] if "Zona" in request_data else ''
        id_empleado = request_data["id_empleado"] if "id_empleado" in request_data else ''
        Estado = request_data["Estado"] if "Estado" in request_data else ''
        Turno = request_data["Turno"] if "Turno" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spI_T_ins_Zona_Empleado_rct] %s , %s , %s ,%s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (idusuario, Zona, Turno, Estado, id_empleado), database=database)

            print("The length of the response is " + str(len(response)))
            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

# ACTUALIZAR UN CAMPO DE ZONAS POR EMPLEADO
    if request.method == 'PUT':

        # print (request.method);
        # id = request.GET["id"] if "id" in request.GET else ''
        idusuario = request_data["idusuario"] if "idusuario" in request_data else ''
        Zona = request_data["Zona"] if "Zona" in request_data else ''
        Turno = request_data["Turno"] if "Turno" in request_data else ''
        Estado = request_data["Estado"] if "Estado" in request_data else ''
        id_empleado = request_data["id_empleado"] if "id_empleado" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spU_T_ins_Zona_Empleado_rct] %s , %s , %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (idusuario, Zona, Turno, Estado, id_empleado), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

# ACTUALIZAR UN CAMPO DE DESCRIPCIONES
    if request.method == 'DELETE':

        # print (request.method);

        # id = request.GET["id"] if "id" in request.GET else ''
        idusuario = request_data["idusuario"] if "idusuario" in request_data else ''

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spD_T_ins_Zona_Empleado_rct] %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (idusuario,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
