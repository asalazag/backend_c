from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def logisticsvars(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAMOS LAS REFERENCIAS EXISTENTES EN LA TABLA (T_Detalle_referencia_CV) DE CONTROL DE VIGENCIAS DE UNA BODEGA INDICADA
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[sps_t_Detalle_referencia_CV_rct] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (bodega,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Items not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)


# ADICIONA UN REGISTRO T_Detalle_referencia_CV
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else ''
        diasvigenciaproveedor = request_data["diasvigenciaproveedor"] if "diasvigenciaproveedor" in request_data else 0
        diasvigenciacedi = request_data["diasvigenciacedi"] if "diasvigenciacedi" in request_data else 0
        cantidadempaque = request_data["cantidadempaque"] if "cantidadempaque" in request_data else 0
        peso = request_data["peso"] if "peso" in request_data else 0
        volumen = request_data["volumen"] if "volumen" in request_data else 0
        stockMin = request_data["stockMin"] if "stockMin" in request_data else 0
        stockMax = request_data["stockMax"] if "stockMax" in request_data else 0
        bodega = request_data["bodega"] if "bodega" in request_data else ''
        listavigencias = request_data["listavigencias"] if "listavigencias" in request_data else ''
        codGrupoPrm = request_data["codGrupoPrm"] if "codGrupoPrm" in request_data else ''
        controlaFechaVencimiento = request_data["controlaFechaVencimiento"] if "controlaFechaVencimiento" in request_data else 0
        alto = request_data["alto"] if "alto" in request_data else 0
        ancho = request_data["ancho"] if "ancho" in request_data else 0
        largo = request_data["largo"] if "largo" in request_data else 0
        url = request_data["url"] if "url" in request_data else ''
        factorEstiba = request_data["factorEstiba"] if "factorEstiba" in request_data else 0
        controlaEstatusCalidad = request_data["controlaEstatusCalidad"] if "controlaEstatusCalidad" in request_data else 0

        
        if productoEAN == '':
            return JsonResponse({"message" : 'Debe ingresar un producto'}, safe=False, status=400)
        if diasvigenciaproveedor == '':
            return JsonResponse({"message" :'Debe ingresar los dias de vigencia del proveedor'}, safe=False, status=400)
        if diasvigenciacedi == '':
            return JsonResponse({"message" :'Debe ingresar los dias de vigencia del cedi'}, safe=False, status=400)
        if cantidadempaque == '':
            return JsonResponse({"message" :'Debe ingresar la cantidad de empaque'}, safe=False, status=400)
        if peso == '':
            return JsonResponse({"message" :'Debe ingresar el peso'}, safe=False, status=400)
        if volumen == '':
            return JsonResponse({"message" :'Debe ingresar el volumen'}, safe=False, status=400)
        if stockMin == '':
            return JsonResponse({"message" :'Debe ingresar el stock minimo'}, safe=False, status=400)
        if stockMax == '':
            return JsonResponse({"message" :'Debe ingresar el stock maximo'}, safe=False, status=400)
        if bodega == '':
            return JsonResponse({"message" :'Debe ingresar la bodega'}, safe=False, status=400)
        if listavigencias == '':
            return JsonResponse({"message" :'Debe ingresar la lista de vigencias'}, safe=False, status=400)
        if alto == '':
            return JsonResponse({"message" :'Debe ingresar el alto'}, safe=False, status=400)
        if ancho == '':
            return JsonResponse({"message" :'Debe ingresar el ancho'}, safe=False, status=400)
        if largo == '':
            return JsonResponse({"message" :'Debe ingresar el largo'}, safe=False, status=400)
        
        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spi_t_detalle_refencia_CV_rct] %s , %s , %s ,%s ,%s, %s, %s , %s , %s ,%s , %s ,%s, %s, %s, %s, %s, %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (productoEAN, diasvigenciaproveedor, diasvigenciacedi, cantidadempaque, peso, volumen, stockMin, stockMax, bodega, listavigencias, codGrupoPrm, controlaFechaVencimiento, alto,ancho,largo,url,factorEstiba,controlaEstatusCalidad), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)

# ACTUALIZAR UN CAMPO DE T_Detalle_referencia_CV
    if request.method == 'PUT':

        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else ''
        diasvigenciaproveedor = request_data["diasvigenciaproveedor"] if "diasvigenciaproveedor" in request_data else 0
        diasvigenciacedi = request_data["diasvigenciacedi"] if "diasvigenciacedi" in request_data else 0
        cantidadempaque = request_data["cantidadempaque"] if "cantidadempaque" in request_data else 0
        peso = request_data["peso"] if "peso" in request_data else 0
        volumen = request_data["volumen"] if "volumen" in request_data else 0
        stockMin = request_data["stockMin"] if "stockMin" in request_data else 0
        stockMax = request_data["stockMax"] if "stockMax" in request_data else 0
        bodega = request_data["bodega"] if "bodega" in request_data else ''
        listavigencias = request_data["listavigencias"] if "listavigencias" in request_data else ''
        codGrupoPrm = request_data["codGrupoPrm"] if "codGrupoPrm" in request_data else ''
        controlaFechaVencimiento = request_data["controlaFechaVencimiento"] if "controlaFechaVencimiento" in request_data else 0
        alto = request_data["alto"] if "alto" in request_data else 0
        ancho = request_data["ancho"] if "ancho" in request_data else 0
        largo = request_data["largo"] if "largo" in request_data else 0
        url = request_data["url"] if "url" in request_data else ''
        factorEstiba = request_data["factorEstiba"] if "factorEstiba" in request_data else 0
        controlaEstatusCalidad = request_data["controlaEstatusCalidad"] if "controlaEstatusCalidad" in request_data else 0

        if productoEAN == '':
            return JsonResponse({"message" : 'Debe ingresar un producto'}, safe=False, status=400)
        if diasvigenciaproveedor == '':
            return JsonResponse({"message" :'Debe ingresar los dias de vigencia del proveedor'}, safe=False, status=400)
        if diasvigenciacedi == '':   
            return JsonResponse({"message" :'Debe ingresar los dias de vigencia del cedi'}, safe=False, status=400)
        if cantidadempaque == '':
            return JsonResponse({"message" :'Debe ingresar la cantidad de empaque'}, safe=False, status=400)
        if peso == '':
            return JsonResponse({"message" :'Debe ingresar el peso'}, safe=False, status=400)
        if volumen == '':
            return JsonResponse({"message" :'Debe ingresar el volumen'}, safe=False, status=400)
        if stockMin == '':
            return JsonResponse({"message" :'Debe ingresar el stock minimo'}, safe=False, status=400)
        if stockMax == '':
            return JsonResponse({"message" :'Debe ingresar el stock maximo'}, safe=False, status=400)
        if bodega == '':
            return JsonResponse({"message" :'Debe ingresar la bodega'}, safe=False, status=400)
        if listavigencias == '':
            return JsonResponse({"message" :'Debe ingresar la lista de vigencias'}, safe=False, status=400)
        if alto == '':
            return JsonResponse({"message" :'Debe ingresar el alto'}, safe=False, status=400)
        if ancho == '':
            return JsonResponse({"message" :'Debe ingresar el ancho'}, safe=False, status=400)
        if largo == '':
            return JsonResponse({"message" :'Debe ingresar el largo'}, safe=False, status=400)
        
        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spu_t_detalle_refencia_CV_rct]  %s , %s , %s ,%s , %s, %s , %s , %s ,%s , %s ,%s, %s, %s, %s, %s, %s,%s, %s'''

        try:
            response = exec_query(sp,
                                  (productoEAN, diasvigenciaproveedor, diasvigenciacedi, cantidadempaque,
                                   peso, volumen, stockMin, stockMax, bodega, codGrupoPrm, controlaFechaVencimiento, alto, ancho, largo, url, factorEstiba,controlaEstatusCalidad,listavigencias), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse({"data":response,"message" : 'Ok'}, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Items not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)


# ACTUALIZAR UN CAMPO DE T_Detalle_referencia_CV
    if request.method == 'DELETE':

        # id = request.GET["id"] if "id" in request.GET else ''
        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else ''
        bodega = request_data["bodega"] if "bodega" in request_data else ''

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spD_t_detalle_refencia_CV_rct] %s , %s'''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(
                sp, (productoEAN, bodega,), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse({"data":response,"message" : 'Ok'}, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Items not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)
