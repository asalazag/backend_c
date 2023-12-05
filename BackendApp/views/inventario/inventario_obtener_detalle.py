from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections

from ...utils import *


@csrf_exempt
def get_Detalle_Inventario(request):
  
    request_data = request._body
    warehouse = request_data['warehouse']
    database = request_data['database']

    if request.method == 'GET':
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        producto = request.GET["producto"] if "producto" in request.GET else ''
        fechainicial = request.GET["fechainicial"] if "fechainicial" in request.GET else ''
        fechafinal = request.GET["fechafinal"] if "fechafinal" in request.GET else ''
        sp = '''

                SET NOCOUNT ON
                EXEC [web].[usp_Obtener_Datos_Inventario]  %s,%s,%s,%s
                '''
        try:

            response = exec_query(
                sp, (bodega,producto,fechainicial,fechafinal,), database=database)
            
            if len(response) == 0:
                raise Exception(404)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Items not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)