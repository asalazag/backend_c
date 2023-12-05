#from asyncio.windows_events import NULL
from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ...utils import *


@csrf_exempt
def autoAduanaList(request):

    request_data = request._body
    warehouse = request_data['warehouse']
    database = request_data['database']

# Conversion de la respuesta al formato que recibe el front
# AGREGA EL DETALLE DE TDA_WMS_DPK
    if request.method == 'GET':
        # id = request.GET["id"] if "id" in request.GET else ''
        estado = request.GET['estado']  if 'estado' in request.GET else None
        print(estado)
        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[usp_ObtenerListaAutoAduana] %s
                '''
        # print (sp)
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (estado,), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'Picking not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)


