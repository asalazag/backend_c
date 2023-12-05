#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def dashboard_estados_actividades(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR LAS LINEAS ADUANADAS POR RANGO DE FECHA POR USUARIO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega= request.GET["bodega"]if "bodega"in request.GET else ''
        tipo= request.GET["tipo"]if "tipo"in request.GET else ''

        if tipo == '':
           return JsonResponse({"message" : 'Ingrese un tipo valido'}, safe=False, status=404)
        if bodega == '':
           return JsonResponse({"message" : 'Ingrese una bodega valida'}, safe=False, status=404)

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[sp_Dashboard_Estados_Actividades]  %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (bodega,tipo,), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)

