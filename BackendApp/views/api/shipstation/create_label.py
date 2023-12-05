from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from BackendApp.utils import exec_query
from settings.models import *
from BackendApp.functions.api import *




@csrf_exempt
def create_label_shipstation(request):

        try:
            request_data = dict(request._body)
            database = request_data['database']
        except Exception as e:
            return JsonResponse({'message' : 'Auth invalid'}, safe=False, status=500)     


        if request.method == 'POST':
            try:
                picking = request.GET.get('picking') if request.GET.get('picking') else None
                fecha_inicial = request.GET.get('fecha_inicial') if request.GET.get('fecha_inicial') else None
                fecha_final = request.GET.get('fecha_final') if request.GET.get('fecha_final') else None
                bodega =  request.GET.get('bodega') if request.GET.get('bodega') else None

                print("picking: ", picking)

                response = create_shipstation_label(database, picking)
                
                response_json = dict(response.json())
                print(response_json)

                if 'error' in response_json:
                     return JsonResponse( {'message' : str(response_json['error'])}, safe=False, status=400)
                
                if response.status_code == 200:
                    print("Estatus 200")

                    sp = f'''select *, ISNULL(f.Valida,0) as EstadoPicking FROM [dbo].[ufn_obtenertblplandespachos_epk_ext_allcompany_RCT] ('{fecha_inicial}', '{bodega}', '{fecha_final}')f where f.picking in ({picking})'''

                    response = exec_query(sp, database=database)
                    print(response)  
                    return JsonResponse(response, safe=False, status=200)

                else:      
                    return JsonResponse(response.json(), safe=False, status=500)

            except Exception as e:   
                return JsonResponse( {'message' : str(e)}, safe=False, status=500)           
        
        