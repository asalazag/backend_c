#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def establecer_cuerentena(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR LOS LOTES EN LISTA
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        lote = request_data["lote"] if "lote" in request_data else ''
        productoean = request_data["productoean"] if "productoean" in request_data else ''
        id_empleado = request_data["id_empleado"] if "id_empleado" in request_data else ''

        
        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[EstableceEstadoCuarentena] %s, %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (lote,productoean,id_empleado), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)
