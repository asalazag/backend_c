#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def crud_epk(request):
    request_data = request._body
    database = request_data['database']
    # Conversion de la respuesta al formato que recibe el front
# AGREGA LAS TABLAS DE ENCABEZADO EPK
    request_data = request._body
    database = request_data['database']



#  CONSULTAR UN PEDIDO REGISTRADO EN EPK Y DPK
    if request.method == 'GET':
        # id = request.GET["id"] if "id" in request.GET else ''       productoEAN             = request_data["productoEAN"] if "productoEAN" in request_data else None

        tipoDocto          = request.GET["tipoDocto"]      if "tipoDocto"      in request.GET else None
        doctoERP           = request.GET["doctoERP"]       if "doctoERP"       in request.GET else None
        numpedido          = request.GET["numpedido"]      if "numpedido"      in request.GET else None
        bodega             = request.GET["bodega"]         if "bodega"      in request.GET else None

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[Select_TDA_WMS_EPKvDPK] %s, %s, %s, %s'''

        print (sp)
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (tipoDocto, doctoERP, numpedido, bodega), database=database)
            print("The length of the response is " + str(len(response)))
            # print (response)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)


# AGREGAR UN ITEM A EPK
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        tipoDocto            = request_data["tipoDocto"] if "tipoDocto" in request_data else None
        doctoERP             = request_data["doctoERP"] if "doctoERP" in request_data else None
        numPedido            = request_data["numPedido"] if "numPedido" in request_data else None
        fechaplaneacion      = request_data["fechaplaneacion"] if "fechaplaneacion" in request_data else None
       
        f_pedido             = request_data["f_pedido"] if "f_pedido" in request_data else None
        item                 = request_data["item"] if "item" in request_data else None        
        nombrecliente        = request_data["nombrecliente"] if "nombrecliente" in request_data else None
        contacto             = request_data["contacto"] if "contacto" in request_data else None
        email                = request_data["email"] if "email" in request_data else None
       
        notas                = request_data["notas"] if "notas" in request_data else None
        ciudaddespacho       = request_data["ciudaddespacho"] if "ciudaddespacho" in request_data else None
        paisDespacho         = request_data["paisDespacho"] if "paisDespacho" in request_data else None
        departamentoDespacho = request_data["departamentoDespacho"] if "departamentoDespacho" in request_data else None
        sucursalDespacho     = request_data["sucursalDespacho"] if "sucursalDespacho" in request_data else None
       
        direccionDespacho    = request_data["direccionDespacho"] if "direccionDespacho" in request_data else None
        idsucursal           = request_data["idsucursal"] if "idsucursal" in request_data else None        
        ciudad               = request_data["ciudad"] if "ciudad" in request_data else None
        pedidoRelacionado    = request_data["pedidoRelacionado"] if "pedidoRelacionado" in request_data else None
        cargue               = request_data["cargue"] if "cargue" in request_data else None
       
        nit                  = request_data["nit"] if "nit" in request_data else None
        estadoPicking        = request_data["estadoPicking"] if "estadoPicking" in request_data else None        
        fechaRegistro        = request_data["fechaRegistro"] if "fechaRegistro" in request_data else None
        fPedido              = request_data["fPedido"] if "fPedido" in request_data else None
        fechTrans            = request_data["fechTrans"] if "fechTrans" in request_data else None
       
        transportadora       = request_data["transportadora"] if "transportadora" in request_data else None
        centroOperacion      = request_data["centroOperacion"] if "centroOperacion" in request_data else None
        picking_batch        = request_data["picking_batch"] if "picking_batch" in request_data else None
        _condicionpago       = request_data["_condicionpago"] if "_condicionpago" in request_data else None
       
        _documentoReferencia = request_data["_documentoReferencia"] if "_documentoReferencia" in request_data else None
        bodega               = request_data["bodega"] if "bodega" in request_data else None
        vendedor2            = request_data["vendedor2"] if "vendedor2" in request_data else None
        numguia              = request_data["numguia"] if "numguia" in request_data else None

        response = []

        # Se agrega el item a la lista
        # sp = '''SET NOCOUNT ON
        #         EXEC [dbo].[Insert_TDA_WMS_EPK_Json_RCT] %s , %s , %s , %s '''


        # sp = '''SET NOCOUNT ON
        #         EXEC [dbo].[Insert_TDA_WMS_EPK_Json_RCT] %s , %s , %s, %s '''


        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[Insert_TDA_WMS_EPK_Json_RCT] %s , %s , %s, %s, %s, %s ,%s, %s, %s, %s,
                                                         %s , %s , %s, %s, %s, %s ,%s, %s, %s, %s,
                                                         %s , %s , %s, %s, %s, %s ,%s, %s, %s, %s,
                                                         %s , %s  '''

        # Query que se hace directamente a la base de datos

        try:

            # print ('estaddo -----')
            # print (sp)

            response = exec_query(
                sp, (
                    tipoDocto,doctoERP,numPedido, fechaplaneacion,
                    f_pedido,item,nombrecliente,contacto,email,
                    notas,ciudaddespacho,paisDespacho,departamentoDespacho,sucursalDespacho,
                    direccionDespacho,idsucursal,ciudad,pedidoRelacionado,cargue,
                    nit,estadoPicking,fechaRegistro,fPedido,fechTrans,
                    transportadora, centroOperacion,picking_batch,_condicionpago,
                    _documentoReferencia,bodega,vendedor2,numguia
                    ), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)
