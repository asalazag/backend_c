#from asyncio.windows_events import NULL
import json
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BackendApp.models import *
from django.utils import timezone

from ...utils import *


@csrf_exempt
def crud_epn(request):
    request_data = request._body
    db_name = request_data['database']
    print(db_name)
    # Conversion de la respuesta al formato que recibe el front
# AGREGA LAS TABLAS DE ENCABEZADO EPK


#  CONSULTAR UN PEDIDO REGISTRADO EN EPK Y DPK
    # if request.method == 'GET':
    #     # id = request.GET["id"] if "id" in request.GET else ''       productoEAN             = request_data["productoEAN"] if "productoEAN" in request_data else None

    #     tipoDocto = request.GET["tipoDocto"] if "tipoDocto" in request.GET else None
    #     doctoERP = request.GET["doctoERP"] if "doctoERP" in request.GET else None
    #     numpedido = request.GET["numpedido"] if "numpedido" in request.GET else None
    #     bodega = request.GET["bodega"] if "bodega" in request.GET else None

    #     response = []
    #     sp = ''' SET NOCOUNT ON
    #          EXEC [web].[Select_TDA_WMS_EPKvDPK] %s, %s, %s, %s'''

    #     print(sp)
    #     # Query que se hace directamente a la base de datos
    #     try:
    #         response = exec_query(
    #             sp, (tipoDocto, doctoERP, numpedido, bodega), database=database)
    #         print("The length of the response is " + str(len(response)))
    #         # print (response)
    #         return JsonResponse(response, safe=False, status=200)

    #     except Exception as e:
    #         print("Server Error!: ", e)
    #         return JsonResponse('Server Error!', safe=False, status=500)


# AGREGAR UN ITEM A EPK
    if request.method == 'POST':

        try:

            if(request_data):
                request_data.pop("database")
                print(request_data)
            else:
                return 'No data to create'

            fields = [field.name for field in VWmsEpn._meta.get_fields()]

            print("okay")
            # Check the fields
            for r in request_data:
                if r not in fields:
                    return JsonResponse(str("Field {} not found".format(r)), safe=False, status=500)

            print("okay")
            final_fields = {}
            for f in fields:
                if f == "fechaplaneacion":
                    final_fields[f] = timezone.now()
                elif f == "fechapedido":
                    final_fields[f] = timezone.now()
                else:
                    final_fields[f] = request_data.get(f, None)

            try:
                try:
                    VWmsEpn.objects.using(db_name).create(**final_fields)

                    return JsonResponse("ok", safe=False, status=200)
                except Exception as e:
                    print(e)
                    return JsonResponse(str(e.__cause__), safe=False, status=500)
            except Exception as e:
                print(e)
                return JsonResponse(str(e.__cause__), safe=False, status=500)
                return str(e.__cause__).lower()
        except Exception as e:
            print(e)
            return JsonResponse(str(e.__cause__), safe=False, status=500)
