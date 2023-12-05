
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def variables_lote(request):
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
        
            query = '''
                    select
                    d.CodigoDescripcion
                    ,d.Descripcion
                    from dbo.T_ins_Descripciones d
                    where grupo ='_ConfigVbleLogistica'
                    '''          
            try:        
                response = exec_query(
                    query,(), database=database)
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
        
        cajano = request_data['cajano'] if 'cajano' in request_data else ''
        ean = request_data['ean'] if 'ean' in request_data else ''
        
        if cajano == '':
           return JsonResponse({"message" : 'Ingrese un numero de lote valido'}, safe=False, status=404)
        else: 
            query = '''
                    SET NOCOUNT ON
                    declare @cajano nvarchar(100)=%s
                    declare @ean nvarchar(100)==%s
                    if (select count(*) from dbo.T_Vbles_LogisticasxCaja where CajaNo=@cajano)=0
                    begin
                    insert into dbo.T_Vbles_LogisticasxCaja (CajaNo,VBL1,VBL2,VBL3,VBL4,VBL5,codean)
                    values(@cajano,'','','','','',@ean)
                    end
                    '''
            query2 = '''
                    select
                    id as id
                    ,vl.CajaNo as loteproveedor
                    ,vl.VBL1 as VBL1
                    ,vl.VBl2 as VBl2
                    ,vl.VBl3 as VBl3
                    ,vl.VBl4 as VBl4
                    ,vl.VBl5 as VBl5
                    ,vl.codean as ean
                    from dbo.T_Vbles_LogisticasxCaja vl
                    where vl.CajaNo=%s                        
                    '''
            try:
                response = exec_query(query, (cajano,ean,), database=database)
            except Exception as e:
                next           
            try:        
                response = exec_query(
                    query2, (cajano,), database=database)
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

        vbl1 = request_data['vbl1'] if 'vbl1' in request_data else ''
        vbl2 = request_data['vbl2'] if 'vbl2' in request_data else ''
        vbl3 = request_data['vbl3'] if 'vbl3' in request_data else ''
        vbl4 = request_data['vbl4'] if 'vbl4' in request_data else ''
        vbl5 = request_data['vbl5'] if 'vbl5' in request_data else ''
        id= request_data['id'] if 'id' in request_data else None   
        
        query = '''
                update vl
                set vl.VBL1 = %s
                    ,vl.VBl2 = %s
                    ,vl.VBl3 = %s
                    ,vl.VBl4 = %s
                    ,vl.VBl5 = %s
                from dbo.T_Vbles_LogisticasxCaja vl
                where vl.id= %s
                '''
        try:
            response = exec_query(
                    query, (vbl1,vbl2,vbl3,vbl4,vbl5,id,), database=database)
        except Exception as e:
            print(e)
            next
        try:
            queryv = '''
                    select
                    vl.id as id
                    ,vl.CajaNo as loteproveedor
                    ,vl.VBL1 as VBL1
                    ,vl.VBl2 as VBl2
                    ,vl.VBl3 as VBl3
                    ,vl.VBl4 as VBl4
                    ,vl.VBl5 as VBl5
                    ,vl.codean as ean
                    from dbo.T_Vbles_LogisticasxCaja vl
                    where vl.id= %s  
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

            

            
