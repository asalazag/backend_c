from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections

from ...utils import *


@csrf_exempt
def cantidad_unidades_empaque(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']

    if request.method == 'GET':
        response = []
        ean = request.GET['ean'] if 'ean' in request.GET else None
        cantidad = request.GET['cantidad'] if 'cantidad' in request.GET else None
        sp = '''SET NOCOUNT ON
             select * from dbo.fnT_CantidadEnUnidadesEmpaqueEAN( %s, %s)'''
        try:

            response = exec_query(sp, (ean,cantidad), database=database)            
            if len(response) == 0:
                raise Exception(404)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'Not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)