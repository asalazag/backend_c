#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def tipodocumento(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR LINEAS NEGADAS POR PROCESO EN PICKING Y ADUANA
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        tabla = request.GET["tabla"] if "tabla" in request.GET else None

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[get_tipo_documentos] %s '''

        tabla = tabla.upper()
        print(tabla)

        if tabla == None:
            return JsonResponse({"error": "No table provided"}, safe=False, status=400)

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (tabla,), database=database)

            array_response = []
            for i in response:
                print(i)
                array_response.append(i['tipoDocto'])

            print("The length of the response is " + str(len(response)))
            return JsonResponse(array_response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)
