#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def crud_euk(request):
    request_data = request._body
    database = request_data['database']
    # Conversion de la respuesta al formato que recibe el front
# AGREGA LAS TABLAS DE ENCABEZADO EPK
    request_data = request._body
    database = request_data['database']



#  CONSULTAR UN PEDIDO REGISTRADO EN EPK Y DPK
    if request.method == 'GET':
        # id = request.GET["id"] if "id" in request.GET else ''       productoEAN             = request_data["productoEAN"] if "productoEAN" in request_data else None

        tipodocto          = request.GET["tipodocto"]      if "tipodocto"      in request.GET else None
        doctoerp           = request.GET["doctoerp"]       if "doctoerp"       in request.GET else None
        numdocumento       = request.GET["numdocumento"]   if "numdocumento"   in request.GET else None
        bodega             = request.GET["bodega"]         if "bodega"         in request.GET else None

        response = []
        # sp = ''' SET NOCOUNT ON
        #      EXEC [web].[Select_TDA_WMS_EUKvDUK] %s, %s, %s, %s'''

        sp = ''' SET NOCOUNT ON
               EXEC [web].[spr_obtenerDuk] %s, %s, %s, %s'''

        print (sp)
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (tipodocto, doctoerp, numdocumento, bodega), database=database)
            print("The length of the response is " + str(len(response)))
            print (response)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)


# AGREGAR UN ITEM A EUK
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        tipoDocto            = request_data["tipoDocto"]    if "tipoDocto"      in request_data else None
        doctoERP             = request_data["doctoERP"]     if "doctoERP"       in request_data else None
        numdocumento         = request_data["numdocumento"] if "numdocumento"   in request_data else None
        fecha                = request_data["fecha"]        if "fecha"          in request_data else None
       
        item                 = request_data["item"]             if "item"               in request_data else None        
        nombreProveedor      = request_data["nombreProveedor"]  if "nombreProveedor"    in request_data else None
        contacto             = request_data["contacto"]         if "contacto"           in request_data else None
        email                = request_data["email"]            if "email"              in request_data else None
       
        nit                       = request_data["nit"]                         if "nit" in request_data else None
        estadodocumentoubicacion  = request_data["estadodocumentoubicacion"]    if "estadodocumentoubicacion" in request_data else None
        Id                        = request_data["Id"]                          if "Id" in request_data else None
        unido                     = request_data["UNIDO"]                       if "UNIDO" in request_data else None
        bodega                    = request_data["bodega"]                      if "bodega" in request_data else None
       
        response = []

        # Se agrega el item a la lista
        # sp = '''SET NOCOUNT ON
        #         EXEC [dbo].[Insert_TDA_WMS_EPK_Json_RCT] %s , %s , %s , %s '''


        # sp = '''SET NOCOUNT ON
        #         EXEC [dbo].[Insert_TDA_WMS_EPK_Json_RCT] %s , %s , %s, %s '''


        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [dbo].[Insert_TDA_WMS_EUK_Json_RCT] %s , %s , %s, %s, %s, %s ,%s, %s, %s, %s,
                                                         %s , %s , %s '''

        # Query que se hace directamente a la base de datos

        try:

            print ('estaddo -----')
            print (sp)

            response = exec_query(
                sp, (
                    tipoDocto,doctoERP,numdocumento, fecha,
                    item,nombreProveedor,contacto,email,
                    nit,estadodocumentoubicacion,Id,unido,bodega
                    ), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)
