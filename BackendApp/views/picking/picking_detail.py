
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def picking_detail(request):
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

        if numpedidos == []:
            return JsonResponse({"error" : "No hay numpedidos"}, safe=False, status=400)


        if numpedidos[0] == "[":
            variable = numpedidos.replace("'", "")
            print(variable)
            variable = variable[1:-1]
        else: 
            variable = numpedidos.replace("'", "")
            print(variable)
            # variable = variable[1:-1].split(",")
        # else:
        #     variable = numpedidos.split(",")
        #     print(variable)
        # numpedidos = list(variable)
        response_ = []
        # if len(numpedidos) >= 1:
        # for numpedido in numpedidos:

        # try:
        #     numpedido = int(numpedido)
        # except:
        #     numpedido = numpedido
        try:
            with connections[database].cursor() as cursor:
                sp = 'usp_T_Narth_Serie_Pedido_ObtenerConUbicacionesFijas_RCT'

                if database == 'pth':
                    sp = 'usp_T_Narth_Serie_Pedido_ObtenerConUbicacionesFijas_RCT_2'

                query = f" SET NOCOUNT ON  EXECUTE [web].[{sp}] '{variable}','{tipoDePlaneacion}','{meses}','{cargue}' , '{bodega}'"

                # query = f" SET NOCOUNT ON  EXECUTE [web].[{sp}] '{numpedido}','{tipoDePlaneacion}','{meses}','{cargue}' , '{bodega}'"
                print(query)
                r = cursor.execute(query)

                columns = [col[0] for col in cursor.description]
                # row = cursor.fetchall()
                data = [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]

        # sp = '''

        #         SET NOCOUNT ON
        #         EXEC [web].[usp_T_Narth_Serie_Pedido_ObtenerConUbicacionesFijas_RCT_2]  %s, %s, %s, %s
        #         '''
        # try:

        #     response = exec_query(
        #         sp, (str(numpedido), int(tipoDePlaneacion), meses, cargue), database=database)
                # response_.extend(data)
                return JsonResponse(data, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)

        # print("The length of the response is " + str(len(response_)))
        # return JsonResponse(response_, safe=False, status=200)
