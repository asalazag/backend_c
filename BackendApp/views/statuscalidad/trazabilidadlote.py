#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
import xmltodict

from ...utils import *


@csrf_exempt
def trazabilidadlote(request):

    request_data = request._body
    database = request_data['database']

#  CONSULTAR LOS LOTES EN LISTA
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        lote = request.GET["lote"] if "lote" in request.GET else ''

        sp = f'''
            select * from T_HistoricoLotes where idlote = '{lote}' '''
        
        try:
            response = exec_query(
                sp, (), database=database)
            print(response)
            
        
        except Exception as e:
            return JsonResponse({"message" : "Error obteniendo T_HistoricoLotes"}, safe=False, status=500)
        

        if len(response) == 0:
            sp = ''' SET NOCOUNT ON
                EXEC [dbo].[prcCrearHistoricoLote] %s'''
            
            try:
                response = exec_query(
                sp, (lote,), database=database)
                print(response)
            
            except Exception as e:
                return JsonResponse({"message" : "Error registrando T_HistoricoLotes"}, safe=False, status=500)
             


        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[prcGetHistoricoLote] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (lote,), database=database)

            response = response[0]['strXML']
            data_dict = xmltodict.parse(response)
            response = json.dumps(data_dict)
            response_json = json.loads(response)
            print(response_json)
            print("The length of the response is " + str(len(response_json)))
            return JsonResponse(response_json, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
