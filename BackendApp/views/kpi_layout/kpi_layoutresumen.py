#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def kpi_layoutresumen(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[kpi_layout] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (bodega,), database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse(e, safe=False, status=500)
