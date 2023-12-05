
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *

@csrf_exempt
def execute_sp(request):
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

        sp = request_data['sp'] if 'sp' in request_data else None
        if sp is None:
            return JsonResponse({"message" : 'sp is required'}, safe=False, status=400)
        if 'drop' in sp.lower():
            return JsonResponse({"message" : 'drop is not allowed'}, safe=False, status=400)
        if 'truncate' in sp.lower():
            return JsonResponse({"message" : 'truncate is not allowed'}, safe=False, status=400)
        if 'delete' in sp.lower():
            return JsonResponse({"message" : 'delete is not allowed'}, safe=False, status=400)
        if 'update' in sp.lower():
            return JsonResponse({"message" : 'update is not allowed'}, safe=False, status=400)
        if 'insert' in sp.lower():
            return JsonResponse({"message" : 'insert is not allowed'}, safe=False, status=400)
        if 'create' in sp.lower():
            return JsonResponse({"message" : 'create is not allowed'}, safe=False, status=400)
        if 'alter' in sp.lower():	
            return JsonResponse({"message" : 'alter is not allowed'}, safe=False, status=400)
        if 'grant' in sp.lower():
            return JsonResponse({"message" : 'grant is not allowed'}, safe=False, status=400)
        if 'revoke' in sp.lower():
            return JsonResponse({"message" : 'revoke is not allowed'}, safe=False, status=400)
        if 'deny' in sp.lower():
            return JsonResponse({"message" : 'deny is not allowed'}, safe=False, status=400)
        if 'backup' in sp.lower():
            return JsonResponse({"message" : 'backup is not allowed'}, safe=False, status=400)
        if 'restore' in sp.lower():
            return JsonResponse({"message" : 'restore is not allowed'}, safe=False, status=400)
        if 'shutdown' in sp.lower():
            return JsonResponse({"message" : 'shutdown is not allowed'}, safe=False, status=400)
        if 'kill' in sp.lower():
            return JsonResponse({"message" : 'kill is not allowed'}, safe=False, status=400)
        
        try:
            response = exec_query(sp,(), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        
        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)

            

            
