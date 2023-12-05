
from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


        
@csrf_exempt
def GetInfoConteneinerByEanOrder(request): 

    try:
        database = request._body["database"] 
    except Exception as e: 
        print(e)
        return JsonResponse('Server Error!', safe=False, status=500)  
    # Get Inventory By Box
    if request.method == 'GET':
        #customs/orders/getinfoconteneinerbyeanorder?npedido=#&eandecaja=#&NumeroTotalDeCajas=#&
        #Look for params
        npedido = request.GET["npedido"] if "npedido" in request.GET else None
        eandecaja = request.GET["eandecaja"] if "eandecaja" in request.GET else None
        NumeroTotalDeCajas = request.GET["NumeroTotalDeCajas"] if "NumeroTotalDeCajas" in request.GET else None
      
        
        #Sp to exec
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_ObtenerInformacionDeContenidoxEanDeCaja_newPedido] %s,%s,%s'''

       #Try to execute
        try:
            response = exec_query(sp, (npedido,eandecaja,NumeroTotalDeCajas,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"message" : 'Not found Item'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)