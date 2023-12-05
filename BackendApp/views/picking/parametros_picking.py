
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def parametros_picking(request):
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
    if request.method == 'GET':

        Controltiquete = request.GET['Controltiquete']  if 'Controltiquete' in request.GET else ''
       
        if Controltiquete == '':
           return JsonResponse({"message" : 'Ingrese un numero de control valido'}, safe=False, status=404)
        else: 
            query = '''
                    SET NOCOUNT ON
                    declare @contoltiqueteprm nvarchar(50) = %s
                    if (select count(*) from dbo.T_ControlDeParametrosxProceso where Controltiquete= @contoltiqueteprm)=0
                    begin 
                                            EXEC dbo.spI_T_ControlDeParametrosCustomized
                        @Controltiquete  = @contoltiqueteprm ,
                        @CodGrupoPrm = 'DPF',
                        @empleado = 'SISTEMAS RYMEL',
                        @numMuestra =1
                        select 
                        cpp.id
                        ,cpp.CodGrupoPrm
                        ,dpc.DescribeParametro
                        ,cpp.Observacion
                        from dbo.T_ControlDeParametrosxProceso cpp
                        inner join dbo.T_ins_DescribeParametrosDeCalidad dpc on cpp.codprm =dpc.CodPrm 
                        where cpp.Controltiquete= @contoltiqueteprm
                    end
                    '''
            query2 = '''
                    select 
                        cpp.id
                        ,cpp.CodGrupoPrm
                        ,dpc.DescribeParametro
                        ,cpp.Observacion
                        from dbo.T_ControlDeParametrosxProceso cpp
                        inner join dbo.T_ins_DescribeParametrosDeCalidad dpc on cpp.codprm =dpc.CodPrm 
                        where cpp.Controltiquete= %s
                    '''
            try:
                response = exec_query(query, (Controltiquete,), database=database)
            except Exception as e:
                next           
            try:        
                response = exec_query(
                    query2, (Controltiquete,), database=database)
                print("The length of the response is " + str(len(response)))
                if len(response) == 0:
                    return JsonResponse({"message" : 'No hay datos para mostrar'}, safe=False, status=404)
                else:
                    return JsonResponse(response, safe=False, status=200)
            
            except Exception as e:
                print("Server Error!: ", e)

                if str(e) == "404":
                    return JsonResponse({"message" : 'not found'}, safe=False, status=404)
                else:
                    return JsonResponse({"message" : str(e)}, safe=False, status=500)
    
    
    if request.method == 'PUT':

        observacion = request_data['observacion'] if 'observacion' in request_data else None
        id= request_data['id'] if 'id' in request_data else None   
        query = '''
                update cp
                set cp.Fechahora = getdate(),
                cp.observacion = %s
                from dbo.T_ControlDeParametrosxProceso cp
                where id= %s
                '''
        try:
            response = exec_query(
                    query, (observacion,id,), database=database)
        except Exception as e:
            print(e)
            next
        try:
            queryv = '''
                    select 
                        cpp.id
                        ,cpp.CodGrupoPrm
                        ,dpc.DescribeParametro
                        ,cpp.Observacion
                        from dbo.T_ControlDeParametrosxProceso cpp
                        inner join dbo.T_ins_DescribeParametrosDeCalidad dpc on cpp.codprm =dpc.CodPrm 
                        where cpp.id= %s and cpp.observacion = %s
                    '''
            response = exec_query(
                queryv, (id,observacion,), database=database)
            
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
            
        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)

            

            
