from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections

from ...utils import *


@csrf_exempt
def get_Data_Resurtido(request):
  
    request_data = request._body
    warehouse = request_data['warehouse']
    database = request_data['database']

    if request.method == 'GET':
        bod = request.GET["bodega"] if "bodega" in request.GET else ''
        sp = '''

                SET NOCOUNT ON
                EXEC [web].[usp_Datos_Resurtido]  %s
                '''
        try:

            response = exec_query(
                sp, (bod,), database=database)
            
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