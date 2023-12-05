from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections

from ...utils import *


@csrf_exempt
def get_Detalle_Resurtido(request):

    request_data = request._body
    warehouse = request_data['warehouse']
    database = request_data['database']

    if request.method == 'GET':
        try:
            bodega = request.GET["bodega"] if "bodega" in request.GET else None
            codigo = request.GET["codigo"] if "codigo" in request.GET else None
        
            if bodega == None:
                return JsonResponse({"message": "bodega is required"}, status=400)
            if codigo == None:
                return JsonResponse({"message": "codigo is required"}, status=400)
            
            sp = '''

                SET NOCOUNT ON
                EXEC [web].[usp_Detalle_Resurtido]  %s, %s
                '''

            response = exec_query(sp, (bodega, codigo,), database=database)

            if len(response) == 0:
                return JsonResponse({"message": "Not found"}, status=500)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse({"message": str(e)}, safe=False, status=400)
