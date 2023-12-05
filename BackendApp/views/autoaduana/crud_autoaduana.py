#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def crud_autoaduana(request):
    request_data = request._body
    database = request_data['database']
    warehouse = request_data['warehouse']
    # Conversion de la respuesta al formato que recibe el front
# AGREGA LAS TABLAS DE ENCABEZADO EPK


#  CONSULTAR UN PEDIDO REGISTRADO EN EPK Y DPK
    if request.method == 'GET':

        if warehouse == '':
            warehouse = None

        picking = request.GET["picking"] if "picking" in request.GET else None

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spr_autoaduanar_picking] %s, %s'''

        print (sp)
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (picking, warehouse), database=database)
            print("The length of the response is " + str(len(response)))
            # print (response)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)


# AGREGAR UN ITEM A EPK
    if request.method == 'POST':

        if warehouse == '':
            warehouse = None

        picking = request.GET["picking"] if "picking" in request.GET else None

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spi_autoaduanar_picking] %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (picking, warehouse), database=database)
            print("The length of the response is " + str(len(response)))
            # print (response)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
   