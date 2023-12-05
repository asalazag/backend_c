
#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def modificalote(request):

    request_data = request._body
    database = request_data['database']

    # ACTUALIZAR EL ESTADO DE CALIDAD DE UN LOTE Y LE ASIGNA EL NUMERO DE CONTROL
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        idLote = request_data["idLote"] if "idLote" in request_data else None
        loteproveedor = request_data["loteproveedor"] if "loteproveedor" in request_data else None
        nitprov = request_data["nitprov"] if "nitprov" in request_data else None
        codEan = request_data["codEan"] if "codEan" in request_data else None
        fechaingresa = request_data["fechaingresa"] if "fechaingresa" in request_data else None
        fechavence = request_data["fechavence"] if "fechavence" in request_data else None
        Confirmacertif = request_data["Confirmacertif"] if "Confirmacertif" in request_data else None
        PedProveedor = request_data["PedProveedor"].strip(
        ) if "PedProveedor" in request_data else None
        Ord_no = request_data["Ord_no"] if "Ord_no" in request_data else None
        Ord_noFactura = request_data["Ord_noFactura"] if "Ord_noFactura" in request_data else None

        response = []

        sp = '''SET NOCOUNT ON
                EXEC [web].[spU_T_Maestro_lote_PT_customized_rct] %s , %s , %s , %s , %s, %s , %s , %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (idLote, loteproveedor, nitprov, codEan, fechaingresa,
                     fechavence, Confirmacertif, PedProveedor, Ord_no, Ord_noFactura,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
