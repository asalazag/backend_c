#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *

@csrf_exempt
def kpi_lineasalmacenadasxrango(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        fechainicial    = request.GET["fechainicial"]       if "fechainicial"   in request.GET else ''
        fechafinal      = request.GET["fechafinal"]         if "fechafinal"     in request.GET else ''
        bodega          = request.GET["bodega"]             if "bodega"         in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[kpi_lineasAlmacenadasxdia] %s, %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (fechainicial,fechafinal,bodega,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)

