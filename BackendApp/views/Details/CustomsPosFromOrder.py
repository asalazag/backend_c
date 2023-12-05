from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from ...utils import *

@csrf_exempt
def CustomsPosFromOrder(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500) 
    request_data = request._body
    # Get Inventory Close to Expiration
    if request.method == 'PUT':
        #customs/orders/customsposfromorder?barcode=#&Cantidad=#&unitarizador=#&IDEmpleado=#&numpedido=#&TipoCaja=#&
        #Look for params
        barcode = str(request_data["barcode"]) if "barcode" in request_data else None
        Cantidad = str(request_data["Cantidad"]) if "Cantidad" in request_data else None
        unitarizador = str(request_data["unitarizador"]) if "unitarizador" in request_data else None
        IDEmpleado = str(request_data["id_employee"]) if "id_employee" in request_data else None
        numpedido = str(request_data["numpedido"]) if "numpedido" in request_data else None
        TipoCaja = str(request_data["TipoCaja"]) if "TipoCaja" in request_data else None
      
        

        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spI_T_Aduana_WMS_POS_FromPedido] %s,%s,%s,%s,%s,%s'''

       #Try to execute
        try:
            print("Executing SP: " + sp)
            print("Params: " + barcode + " " + Cantidad + " " + unitarizador + " " + IDEmpleado + " " + numpedido + " " + TipoCaja)
            response = exec_query(sp, (barcode,Cantidad,unitarizador,IDEmpleado,numpedido,TipoCaja,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Items not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)