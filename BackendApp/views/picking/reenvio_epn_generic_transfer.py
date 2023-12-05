import requests
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def reenvio_epn_generic_transfer(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    warehouse = request_data['warehouse']
    database = request_data['database']

    # GET se envian los parametros por query params. 
    # para capturar = request.GET['parametro'] eje: request.GET['picking'] 
    # El put se usa para actualizar la información. 
    # se usa el cuerpo para traer la información a actualizar
    # para capturar el cuerpo request_data['parametro'] eje:  request_data['picking']
    if request.method == 'POST':

        bodega = request_data['bodega'] if 'bodega' in request_data else None
        tipodocto = request_data['tipodocto'] if 'tipodocto' in request_data else None
        doctoerp = request_data['doctoerp'] if 'doctoerp' in request_data else None
        caja = request_data['caja'] if 'caja' in request_data else None
        
        if bodega == None:
            return JsonResponse({"message" : "Bodega is required"}, safe=False, status=400)
        if tipodocto == None:
            return JsonResponse({"message" : "Tipodocto is required"}, safe=False, status=400)
        if doctoerp == None:
            return JsonResponse({"message" : "Doctoerp is required"}, safe=False, status=400)
        if caja == None:
            return JsonResponse({"message" : "Caja is required"}, safe=False, status=400)
        
        APIKEY = 'gBv9L551yKI-UiaHIZvkltUniJvR1dcaVERMVDVBUGyzfhCY6YZGf6z0sHjncHX9ilg'
        
        url = 'https://api.copernicowms.com/'
        endpoint = 'generic_transfer_siesa/entrega_produccion'
        
        
        headers = {
            'Authorization': APIKEY
        }
        
        query_params = {
            "bodega" : bodega,
            "tipodocto" : tipodocto,
            "doctoerp" : doctoerp,
            "caja" : caja
        }
        
        try:
            
            response = requests.post(url + endpoint ,params=query_params, headers=headers)   
            return JsonResponse(response.json(), safe=False, status=200)
        
        except Exception as e:
            print("Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"response" : 'Not found'}, safe=False, status=404)
            else:
                return JsonResponse({"response" : str(e)}, safe=False, status=500)
    












