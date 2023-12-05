from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def groups(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spS_t_ins_grupos] '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
