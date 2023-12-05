
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def lotes_picking(request):
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
    # if request.method == 'GET':

    #     employee = request.GET['employee']  if 'employee' in request.GET else ''
    #     sp = '''

    #             SET NOCOUNT ON
    #             EXEC [web].[spS_TempleadosPK]  %s
    #             '''
    #     try:
    #         response = exec_query(
    #             sp, (employee,), database=database)
            
    #         if len(response) == 0:
    #             raise Exception(404)

    #         print("The length of the response is " + str(len(response)))
    #         return JsonResponse(response, safe=False, status=200)

    #     except Exception as e:
    #         print("Server Error!: ", e)

    #         if str(e) == "404":
    #             return JsonResponse({"message" : 'not found'}, safe=False, status=404)
    #         else:
    #             return JsonResponse({"message" : str(e)}, safe=False, status=500)
    
    
    if request.method == 'POST':

        inicio = request_data['inicio'] if 'inicio' in request_data else None
        final = request_data['final'] if 'final' in request_data else None
        id_usuario = request_data['id_usuario'] if 'id_usuario' in request_data else None
            
        sp = '''

                SET NOCOUNT ON
                EXEC [web].[usp_crearLotesDesdeOPExterna_1] %s, %s, %s
                '''
        try:

            response = exec_query(
                sp, (inicio,final,id_usuario,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        
        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)

            

            
