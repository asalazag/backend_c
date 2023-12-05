from urllib import request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from datetime import date
from ...utils import *

# CARGAMOS LA TABLA DE PLAN DESPACHOS


@csrf_exempt
def getplanrecibo(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']
    role = request_data['role']

    if request.method == 'GET':
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        fecha_inicial = request.GET["fecha_inicial"] if "fecha_inicial" in request.GET else None
        fecha = request.GET["fecha"] if "fecha" in request.GET else None
        fecha_final = request.GET["fecha_final"] if "fecha_final" in request.GET else None
        metodo = request.GET["metodo"] if "metodo" in request.GET else 0
        parametro = request.GET["parametro"] if "parametro" in request.GET else None
        tipodeplaneacion = request.GET["tipodeplaneacion"] if "tipodeplaneacion" in request.GET else 0
        tipodocto = request.GET["tipodocto"] if "tipodocto" in request.GET else None
        id_customer = request_data['id_customer'] if "id_customer" in request_data else ''


        response = []

        sp = '''SET NOCOUNT ON
            EXEC [web].[usp_ObtenerTblPlanRecibo_RCT] %s, %s, %s, %s, %s, %s, %s, %s'''

        # Query que se hace directamente a la base de datos
        if fecha is not None:
            fecha = fecha.replace("-", "")
        try:
            response = exec_query(
                sp, (bodega, fecha_inicial, metodo, parametro, tipodeplaneacion, tipodocto, fecha_final, id_customer), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
      
