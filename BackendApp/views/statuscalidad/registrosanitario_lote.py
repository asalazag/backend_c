
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def registrosanitario_lote(request):
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
        
        loteproveedor = request.GET['loteproveedor']  if 'loteproveedor' in request.GET else ''
        ean = request.GET['ean']  if 'ean' in request.GET else ''

        if loteproveedor == '':
           return JsonResponse({"message" : 'Ingrese un lote valido'}, safe=False, status=404)
        else: 
            query = '''
                    SELECT [id]
                        ,[loteproveedor]
                        ,[cod_Registro]
                        ,[cod_EAN]
                    FROM [dbo].[T_registroSanitarioxLote]
                    where loteproveedor =%s and cod_EAN =%s               
                    '''      
            try:        
                response = exec_query(
                    query, (loteproveedor,ean,), database=database)
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
    

    
    if request.method == 'POST':
        
        loteproveedor = request_data['loteproveedor'] if 'loteproveedor' in request_data else ''
        ean = request_data['ean'] if 'ean' in request_data else ''
        cod_Registro = request_data['cod_Registro'] if 'cod_Registro' in request_data else ''
        
        
        if loteproveedor == '':
           return JsonResponse({"message" : 'Ingrese un lote valido'}, safe=False, status=404)
        else: 
            query = '''
                    SET NOCOUNT ON
                    declare @loteproveedor nvarchar(100) =%s
                    declare @ean nvarchar(100)=%s
                    declare @codigo nvarchar(100)=%s

                    insert into dbo.T_registroSanitarioxLote (loteproveedor,cod_Registro,cod_EAN)
                    values(@loteproveedor,@codigo,@ean)

                    '''
            query2 = '''
                    SELECT [id]
                        ,[loteproveedor]
                        ,[cod_Registro]
                        ,[cod_EAN]
                    FROM [dbo].[T_registroSanitarioxLote]
                    where loteproveedor =%s and cod_EAN =%s               
                    '''
            try:
                response = exec_query(query, (loteproveedor,ean,cod_Registro,), database=database)
            except Exception as e:
                next           
            try:        
                response = exec_query(
                    query2, (loteproveedor,ean,), database=database)
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

        cod_Registro = request_data['cod_Registro'] if 'cod_Registro' in request_data else ''
        id= request_data['id'] if 'id' in request_data else None   
        
        query = '''
                update rl
                set rl.cod_Registro = %s
                from dbo.T_registroSanitarioxLote rl
                where rl.id= %s
                '''
        try:
            response = exec_query(
                    query, (cod_Registro,id,), database=database)
        except Exception as e:
            print(e)
            next
        try:
            queryv = '''
                    SELECT [id]
                        ,[loteproveedor]
                        ,[cod_Registro]
                        ,[cod_EAN]
                    FROM [dbo].[T_registroSanitarioxLote]
                    where id= %s 
                    '''
            response = exec_query(
                queryv, (id,), database=database)
            
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
            
        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)

            

            
