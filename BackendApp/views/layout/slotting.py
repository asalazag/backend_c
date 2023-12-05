#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def slotting(request):

    request_data = request._body
    database = request_data['database']


# CREA UNA LINEA DE TAREA DE SLOTTING CON BASE EN EL REGISTRO ENVIADO
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        caja = request_data["caja"] if "caja" in request_data else 0
        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else ''
        bodega = request_data["bodega"] if "bodega" in request_data else ''

        response = []

        # print (request_data["permisosApp"])

        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_planningSlotTaskByBox] %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (caja, productoEAN, bodega), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            print(response)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
