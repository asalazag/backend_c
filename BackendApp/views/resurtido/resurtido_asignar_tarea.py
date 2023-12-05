from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections

from ...utils import *


@csrf_exempt
def resurtido_asignar_tarea(request):

    request_data = request._body
    database = request_data['database']
    usuario = request_data['id_employee']

    if request.method == 'POST':

        ean = request_data["ean"] if "ean" in request_data else None
        empleado = request_data["empleado"] if "empleado" in request_data else ""
        cantidad = request_data["cantidad"] if "cantidad" in request_data else None
        bodega = request_data["bodega"] if "bodega" in request_data else None

        sp = '''
                SET NOCOUNT ON
                EXEC [web].[usp_Add_Tarea_Resurtido]  %s, %s, %s, %s, %s
                '''
        try:

            response = exec_query(sp, (bodega,ean,empleado,cantidad,usuario), database=database)            
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse({"message" : str(e)}, safe=False, status=400)