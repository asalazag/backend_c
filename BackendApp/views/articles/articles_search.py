from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *
        
@csrf_exempt
def articles_search(request): 

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        descripcion = request.GET["descripcion"] if "descripcion" in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_searchbydescription] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (descripcion,), database=database)
            return JsonResponse(response, safe=False, status=200)
            # response = exec_query(sp,Any=() ,database=database)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)