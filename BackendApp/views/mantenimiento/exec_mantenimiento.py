
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def execute_mantemimiento(request):
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
        
        destination = request.GET.get('destination', None)

        if destination == None:
            return JsonResponse({"message" : "Destination is required"}, safe=False, status=400)
            

        sp = '''

                SET NOCOUNT ON
                EXEC [dbo].[usp_ejecuta_plan_mantenimiento] 
                '''
        try:

            exec_query(
                sp, (), database=destination)
        
            
            sp = '''

                    SET NOCOUNT ON
                    EXEC [dbo].[usp_ejecuta_plan_mantenimiento_memoria_log] 
                    '''
            try:

                exec_query(
                    sp, (), database=destination)
                
                return JsonResponse({"message" : "ok"}, safe=False, status=200)
            
            except Exception as e:   
                print("Server Error!: ", e)
                return JsonResponse({"message" : str(e)}, safe=False, status=500)



        except Exception as e:   
            print("Server Error!: ", e)
            return JsonResponse({"message" : str(e)}, safe=False, status=500)


            

            
