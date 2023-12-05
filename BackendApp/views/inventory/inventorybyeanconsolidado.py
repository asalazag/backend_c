from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def inventorybyeanconsolidado(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        ean = request.GET["ean"] if "ean" in request.GET else None
        ref = request.GET["ref"] if "ref" in request.GET else None
        bod = request.GET["bod"] if "bod" in request.GET else None

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[dwh_usp_ObtenerDsInventariosxEANWmsConsolidado] %s, %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (ean, ref, bod,), database=database)
            # return JsonResponse(response, safe=False, status=200)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
