from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *
        
@csrf_exempt
def descriptionsbygroup(request): 

    request_data = request._body
    database = request_data['database']


#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        Grupo = request.GET["grupo"] if "grupo" in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spS_T_ins_descripciones] %s'''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spS_T_ins_descripciones] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (Grupo,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)