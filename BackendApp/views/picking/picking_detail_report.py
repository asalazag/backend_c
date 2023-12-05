
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def picking_detail_report(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']

    if request.method == 'GET':
        numpedidos = request.GET["numpedido"] if "numpedido" in request.GET else [
        ]
        tipoDePlaneacion = request.GET["tipoDePlaneacion"] if "tipoDePlaneacion" in request.GET else 0
        meses = request.GET["meses"] if "meses" in request.GET else 0
        cargue = request.GET["cargue"] if "cargue" in request.GET else 0
        bodega = request.GET["bodega"] if "bodega" in request.GET else None

        print("numpedidos: ", numpedidos)
        # numpedidos = list(numpedidos)

        try:
            with connections[database].cursor() as cursor:
                sp = 'usp_T_Narth_Serie_Pedido_ObtenerConUbicacionesFijas_RCT_UNIFICADO'

                query = f" SET NOCOUNT ON  EXECUTE [web].[{sp}] '{numpedidos}','{tipoDePlaneacion}','{meses}','{cargue}' , '{bodega}'"
                print(query)
                r = cursor.execute(query)

                columns = [col[0] for col in cursor.description]
                # row = cursor.fetchall()
                data = [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]

                response_ = data

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)

        print("The length of the response is " + str(len(response_)))
        return JsonResponse(response_, safe=False, status=200)
