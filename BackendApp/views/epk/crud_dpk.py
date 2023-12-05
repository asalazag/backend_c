#from asyncio.windows_events import NULL
from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def crud_dpk(request):

    request_data = request._body
    database = request_data['database']

# Conversion de la respuesta al formato que recibe el front
# AGREGA EL DETALLE DE TDA_WMS_DPK
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        Referencia = request_data["Referencia"] if "Referencia" in request_data else None
        RefPadre = request_data["RefPadre"] if "RefPadre" in request_data else None
        Descripcion = request_data["Descripcion"] if "Descripcion" in request_data else None
        qtyPedido = request_data["qtyPedido"] if "qtyPedido" in request_data else None
        qtyReservado = request_data["qtyReservado"] if "qtyReservado" in request_data else None

        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else None
        LineaIdPicking = request_data["LineaIdPicking"] if "LineaIdPicking" in request_data else None
        Costo = request_data["Costo"] if "Costo" in request_data else None
        Bodega = request_data["Bodega"] if "Bodega" in request_data else None

        tipoDocto = request_data["tipoDocto"] if "tipoDocto" in request_data else None
        doctoERP = request_data["doctoERP"] if "doctoERP" in request_data else None
        qtyenpicking = request_data["qtyenpicking"] if "qtyenpicking" in request_data else None
        estadodetransferencia = request_data["estadodetransferencia"] if "estadodetransferencia" in request_data else None
        fechaRegistro = request_data["fechaRegistro"] if "fechaRegistro" in request_data else None

        ubicacion_plan = request_data["ubicacion_plan"] if "ubicacion_plan" in request_data else None
        fechatransferencia = request_data["fechatransferencia"] if "fechatransferencia" in request_data else None
        clasifart = request_data["clasifart"] if "clasifart" in request_data else None
        serial = request_data["serial"] if "serial" in request_data else None
        item = request_data["item"] if "item" in request_data else None

        idCo = request_data["idCo"] if "idCo" in request_data else None
        qtyRemisionado = request_data["qtyRemisionado"] if "qtyRemisionado" in request_data else None
        qtyFacturado = request_data["qtyFacturado"] if "qtyFacturado" in request_data else None
        precioUnitario = request_data["precioUnitario"] if "precioUnitario" in request_data else None
        notasitem = request_data["notasitem"] if "notasitem" in request_data else None

        descripcionCo = request_data["descripcionCo"] if "descripcionCo" in request_data else None
        factor = request_data["factor"] if "factor" in request_data else None
        numpedido = request_data["numpedido"] if "numpedido" in request_data else None
        pedproveedor = request_data["pedproveedor"] if "pedproveedor" in request_data else None
        loteproveedor = request_data["loteproveedor"] if "loteproveedor" in request_data else None

        _qtypedidabase = request_data["_qtypedidabase"] if "_qtypedidabase" in request_data else None
        lineaIdPickingInt = request_data["lineaIdPickingInt"] if "lineaIdPickingInt" in request_data else None

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[Insert_TDA_WMS_DPK_Json_RCT] %s , %s , %s, %s, %s, %s ,%s, %s, %s, %s,
                                                         %s , %s , %s, %s, %s, %s ,%s, %s, %s, %s,
                                                         %s , %s , %s, %s, %s, %s ,%s, %s, %s, %s,
                                                         %s '''

        # print (sp)
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (
                    Referencia, RefPadre, Descripcion, qtyPedido, qtyReservado,
                    productoEAN, LineaIdPicking, Costo, Bodega,
                    tipoDocto, doctoERP, qtyenpicking, estadodetransferencia, fechaRegistro,
                    ubicacion_plan, fechatransferencia, clasifart, serial, item,
                    idCo, qtyRemisionado, qtyFacturado, precioUnitario, notasitem,
                    descripcionCo, factor, numpedido, pedproveedor, loteproveedor,
                    _qtypedidabase, lineaIdPickingInt
                ), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)


# BORRAR UN REGISTRO DE LA TDA_WMS_DPK
    if request.method == 'DELETE':

        # id = request.GET["id"] if "id" in request.GET else ''       productoEAN             = request_data["productoEAN"] if "productoEAN" in request_data else None
        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else None
        tipoDocto = request_data["tipoDocto"] if "tipoDocto" in request_data else None
        doctoERP = request_data["doctoERP"] if "doctoERP" in request_data else None
        numpedido = request_data["numPedido"] if "numPedido" in request_data else None

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[Delete_TDA_WMS_DPK_Json_RCT] %s , %s , %s, %s '''

        print(sp)
        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(
                sp, (productoEAN, tipoDocto, doctoERP, numpedido), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)
