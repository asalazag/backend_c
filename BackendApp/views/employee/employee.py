from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def employee(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        id = request_data["id"] if "id" in request_data else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[sp_empleadosxID] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (id,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

            # ACTUALIZAR UN CAMPO DE UN EMPLEADO
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        permisosApp = request_data["permisosApp"] if "permisosApp" in request_data else ''
        corporacion = request_data["corporacion"] if "corporacion" in request_data else ''
        idempleado = request_data["idempleado"] if "idempleado" in request_data else 0

        response = []

        # print (request_data["permisosApp"])

        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_actualizarPermisosAppxIdEmpleado] %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (permisosApp, corporacion, idempleado), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
