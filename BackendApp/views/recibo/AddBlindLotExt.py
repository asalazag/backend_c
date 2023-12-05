from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections
from ...utils import *

@csrf_exempt
def AddBlindLotExt(request): 

    request_data = request._body
    database = request_data['database'] 
    request_data = request._body
    # Get Inventory Close to Expiration
    if request.method == 'POST':
        #receiveandlocate/addblindlotext
        #Look for params
        documentooc = request_data["documentooc"] if "documentooc" in request_data else None
        nit = request_data["nit"] if "nit" in request_data else None
        ean = request_data["ean"] if "ean" in request_data else None
        pedido = request_data["pedido"] if "pedido" in request_data else None
        fvence = request_data["fvence"] if "fvence" in request_data else None
        cantCajas = request_data["cantCajas"] if "cantCajas" in request_data else None
        factor = request_data["factor"] if "factor" in request_data else None
        employee = request_data["employee"] if "employee" in request_data else None
        barcode = request_data["barcode"] if "barcode" in request_data else None
        ord_no = request_data["ord_no"] if "ord_no" in request_data else None
        tipoDoc = request_data["tipoDoc"] if "tipoDoc" in request_data else None
        lineaPicking = request_data["lineaPicking"] if "lineaPicking" in request_data else None
        cajamp = request_data["cajamp"] if "cajamp" in request_data else None
        fromAgregaCajayUbica = request_data["fromAgregaCajayUbica"] if "fromAgregaCajayUbica" in request_data else None
        peso = request_data["peso"] if "peso" in request_data else None
        volumen = request_data["volumen"] if "volumen" in request_data else None
        dim_x = request_data["dim_x"] if "dim_x" in request_data else None
        dim_y = request_data["dim_y"] if "dim_y" in request_data else None
        dim_z = request_data["dim_z"] if "dim_z" in request_data else None
        
        #Sp to exec
        try:
            if database == 'btp' or database == 'sandboxbbl':
                sp = ''' SET NOCOUNT ON
                    EXEC [web].[usp_ingloteciego_extendido] %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s'''
            
                response = exec_query(sp, (documentooc,nit,ean,pedido,fvence,cantCajas,factor,employee,barcode,ord_no,tipoDoc,lineaPicking,cajamp,fromAgregaCajayUbica,peso,volumen,dim_x,dim_y,dim_z,), database=database)
                return JsonResponse(response, safe=False, status=200)
            else:
                sp = ''' SET NOCOUNT ON
                    EXEC [web].[usp_ingloteciego_extendido] %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'''
                response = exec_query(sp, (documentooc,nit,ean,pedido,fvence,cantCajas,factor,employee,barcode,ord_no,tipoDoc,lineaPicking,cajamp,fromAgregaCajayUbica,), database=database)
                return JsonResponse(response, safe=False, status=200)
       #Try to execute
        # try:
        #     response = exec_query(sp, (documentooc,nit,ean,pedido,fvence,cantCajas,factor,employee,barcode,ord_no,tipoDoc,lineaPicking,cajamp,fromAgregaCajayUbica,peso,volumen,), database=database)
        #     return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)