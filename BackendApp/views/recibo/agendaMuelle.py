from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def agendaMuelle(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAMOS LA AGENDA DE MUELLES CORRESPONDIENTES
    if request.method == 'GET':

        id = request.GET["id"] if "id" in request.GET else ''
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        fecha = request.GET["fecha"] if "fecha" in request.GET else ''
        response = []
        try:
            if id == '':
                sp = ''' SET NOCOUNT ON
                declare @fecha date = %s
                select * from dbo.T_plan_agendamuelle where bodega =%s
                and CONVERT(NVARCHAR(8),hora_plan_inicia,112)=convert(nvarchar(8),@fecha,112)
                '''
                response = exec_query(sp, (fecha,bodega,), database=database)
                print("The length of the response is " + str(len(response)))
                return JsonResponse(response, safe=False, status=200)
            else:
                sp = ''' SET NOCOUNT ON
                select * from dbo.T_plan_agendamuelle where id =%s'''
                response = exec_query(sp, (id,), database=database)
                print("The length of the response is " + str(len(response)))
                return JsonResponse(response, safe=False, status=200)

            
            
        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)


# ADICIONA UNA AGENDA DE MUELLES
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega = request_data["bodega"] if "bodega" in request_data else None
        transaccion = request_data["transaccion"] if "transaccion" in request_data else None
        puerta = request_data["puerta"] if "puerta" in request_data else None
        hora_plan_inicia = request_data["hora_plan_inicia"] if "hora_plan_inicia" in request_data else None
        hora_plan_finaliza = request_data["hora_plan_finaliza"] if "hora_plan_finaliza" in request_data else None
        nombre_tercero = request_data["nombre_tercero"] if "nombre_tercero" in request_data else None
        doctoERP = request_data["doctoERP"] if "doctoERP" in request_data else ''
        transportadora = request_data["transportadora"] if "transportadora" in request_data else ''
        placa_vehiculo = request_data["placa_vehiculo"] if "placa_vehiculo" in request_data else ''
        nombre_conductor = request_data["nombre_conductor"] if "nombre_conductor" in request_data else ''
        documento_conductor = request_data["documento_conductor"] if "documento_conductor" in request_data else ''
        telefono_conductor = request_data["telefono_conductor"] if "telefono_conductor" in request_data else ''
        peso_vehiculo = request_data["peso_vehiculo"] if "peso_vehiculo" in request_data else None
        cantidad_pallet = request_data["cantidad_pallet"] if "cantidad_pallet" in request_data else None
        cantidad_caja = request_data["cantidad_caja"] if "cantidad_caja" in request_data else None
        estado = request_data["estado"] if "estado" in request_data else 0
        observaciones = request_data["observaciones"] if "observaciones" in request_data else ''
        
        if hora_plan_finaliza == None or hora_plan_finaliza == None or bodega == None or transaccion == None or puerta == None or nombre_tercero == None:
            return JsonResponse({"message" : 'Ingrese todos los campos obligatorios'}, safe=False, status=404)
        
        
        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
        INSERT INTO [dbo].[T_plan_agendamuelle]
           ([bodega]
           ,[transaccion]
           ,[puerta]
           ,[hora_plan_inicia]
           ,[hora_plan_finaliza]
           ,[doctoERP]
           ,[nombre_tercero]
           ,[transportadora]
           ,[placa_vehiculo]
           ,[nombre_conductor]
           ,[documento_conductor]
           ,[telefono_conductor]
           ,[peso_vehiculo]
           ,[cantidad_pallet]
           ,[cantidad_caja]
           ,[estado]
           ,[observaciones])
     VALUES
           (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)    '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (bodega,transaccion,puerta,hora_plan_inicia,hora_plan_finaliza,doctoERP,nombre_tercero,transportadora,placa_vehiculo,nombre_conductor,documento_conductor,telefono_conductor,peso_vehiculo,cantidad_pallet,cantidad_caja,estado,observaciones,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            print(e)
            next
        try:
            queryv = '''
                    SELECT * FROM [dbo].[T_plan_agendamuelle]
                    where bodega =%s and transaccion =%s and puerta =%s and hora_plan_inicia =%s and hora_plan_finaliza =%s
                    '''
            response = exec_query(
                queryv, (bodega,transaccion,puerta,hora_plan_inicia,hora_plan_finaliza,), database=database)
            if response == []:
                return JsonResponse({"message" : 'No se puede crear el Registro'}, safe=False, status=404)
            else:
                print("The length of the response is " + str(len(response)))
                return JsonResponse(response, safe=False, status=200)
        
        # Query de validacion
        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)
            


# ACTUALIZAR LA INFORMACION DE UNA AGENDA DE MUELLES
    if request.method == 'PUT':

        id = request_data["id"] if "id" in request_data else 0
        bodega = request_data["bodega"] if "bodega" in request_data else None
        transaccion = request_data["transaccion"] if "transaccion" in request_data else None
        puerta = request_data["puerta"] if "puerta" in request_data else None
        hora_plan_inicia = request_data["hora_plan_inicia"] if "hora_plan_inicia" in request_data else None
        hora_plan_finaliza = request_data["hora_plan_finaliza"] if "hora_plan_finaliza" in request_data else None
        nombre_tercero = request_data["nombre_tercero"] if "nombre_tercero" in request_data else None
        doctoERP = request_data["doctoERP"] if "doctoERP" in request_data else ''
        transportadora = request_data["transportadora"] if "transportadora" in request_data else ''
        placa_vehiculo = request_data["placa_vehiculo"] if "placa_vehiculo" in request_data else ''
        nombre_conductor = request_data["nombre_conductor"] if "nombre_conductor" in request_data else ''
        documento_conductor = request_data["documento_conductor"] if "documento_conductor" in request_data else ''
        telefono_conductor = request_data["telefono_conductor"] if "telefono_conductor" in request_data else ''
        peso_vehiculo = request_data["peso_vehiculo"] if "peso_vehiculo" in request_data else None
        cantidad_pallet = request_data["cantidad_pallet"] if "cantidad_pallet" in request_data else None
        cantidad_caja = request_data["cantidad_caja"] if "cantidad_caja" in request_data else None
        estado = request_data["estado"] if "estado" in request_data else 0
        observaciones = request_data["observaciones"] if "observaciones" in request_data else ''
        response = []

        # Se actualiza el item a la lista
        sp = '''SET NOCOUNT ON
                declare @id int= %s
                declare @estado int = %s
                UPDATE [dbo].[T_plan_agendamuelle]
                   SET [bodega] = %s
                   ,[transaccion] = %s
                   ,[puerta] = %s
                   ,[hora_plan_inicia] = %s
                   ,[hora_plan_finaliza] = %s
                   ,[doctoERP] = %s
                   ,[nombre_tercero] = %s
                   ,[transportadora] = %s
                   ,[placa_vehiculo] = %s
                   ,[nombre_conductor] = %s
                   ,[documento_conductor] = %s
                   ,[telefono_conductor] = %s
                   ,[peso_vehiculo] = %s
                   ,[cantidad_pallet] = %s
                   ,[cantidad_caja] = %s
                   ,[estado] = @estado
                   ,[observaciones] = %s
                    WHERE id = @id
                    if @estado = 1
                    begin
                    update [dbo].[T_plan_agendamuelle]
                    set hora_finaliza = GETDATE()
                    where id = @id
                    end
                    '''
                    
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (id,estado,bodega,transaccion,puerta,hora_plan_inicia,hora_plan_finaliza,doctoERP,nombre_tercero,transportadora,placa_vehiculo,nombre_conductor,documento_conductor,telefono_conductor,peso_vehiculo,cantidad_pallet,cantidad_caja,observaciones,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print(e)
            next
        try:
            queryv = '''
                    SELECT * FROM [dbo].[T_plan_agendamuelle]
                    where id =%s
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


# ELIMINA UNA AGENDA DE MUELLES
    if request.method == 'DELETE':

        # print (request.method);

        id = request.GET["id"] if "id" in request.GET else ''
        
        response = []

        # Query que se hace directamente a la base de datos
        sp = '''SET NOCOUNT ON
                delete from [dbo].[T_plan_agendamuelle]
                where id = %s
                '''
        try:

            response = exec_query(sp, (id,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)
