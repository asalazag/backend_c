from copy import deepcopy
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BackendApp.utils import *


@csrf_exempt
def picking_order(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']

    if request.method == 'GET':
        response = []
        sp = '''SET NOCOUNT ON
             select next value for secuencia_cargue as proxcargue'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)

    if request.method == 'POST':
        """
            Para poder apreciar si la orden fue creada correctamente se deben consultar las siguientes tablas

            select *
            from t_materiales_por_orden
            where orden = '25706'

            select * from T_SeriePedido
            where ORDENPDN = '25706'

            Para eliminar: 
            delete
            from T_SeriePedido
            where ORDENPDN = '25706'

        """
        # 10 hace equivalencia a EPK y 11 hace equivalencia a EPN
        plan_type = request_data["plan_type"] if "plan_type" in request_data else 0

        picking_model = request_data["picking_model"] if "picking_model" in request_data else ''
        
        # Código de la bodega
        warehouse_code = request_data["warehouse_code"] if "warehouse_code" in request_data else ''

        # Lista con los pickingERP
        origin_picking = request_data["origin_picking"] if "origin_picking" in request_data else [
        ]

        if not plan_type or plan_type == 0:
            return JsonResponse('plan_type field is required', safe=False, status=400)
        
        if not picking_model or picking_model == '':
            return JsonResponse('picking_model field is required', safe=False, status=400)

        if not warehouse_code or warehouse_code == '':
            return JsonResponse('warehouse_code field is required', safe=False, status=400)

        if not warehouse_code or len(origin_picking) == 0:
            return JsonResponse('origin_picking field is required', safe=False, status=400)

        response = []
        query_response = []

        try:
            
            picking_list = deepcopy(origin_picking)
            picking_list = str(picking_list).replace('[', '').replace(']', '').replace("'", "")

            sp = '''
                        SET NOCOUNT ON
                        EXEC [dbo].[validaExistePickingActivo] %s
            '''

            # Query que se hace directamente a la base de datos
            try:
                query_response = exec_query(sp, (picking_list,), database=database)
                print('VALIDACION OK')
            
            except Exception as e:
                print(e)
                print('VALIDACION FAILED')
                return JsonResponse({"message" : str(e)}, safe=False, status=400)
        
        except Exception as e:
            print(e)
            print('VALIDACION FAILED')
            return JsonResponse({"message" : str(e)}, safe=False, status=400)

        if picking_model == 'order':
            for o in origin_picking:
                # Corregir si se elije epn

                if str(plan_type) == "10":

                    sp = 'select tipodocto, doctoerp, numpedido from v_wms_epk where picking=%s'
                
                elif str(plan_type) == "11":

                    sp = 'select tipodocto, doctoerp, numpedido from v_wms_epn where picking=%s'
                
                else:
                    return JsonResponse('plan type is invalid', safe=False, status=400)
                # f'''select * FROM [ufn_obtenertblplandespachos_epk_ext_allcompany] ('{format_today}', '{warehouse_code}')f where f.OrdenDespacho ={p}'''
                # Query que se hace directamente a la base de datos
                try:
                    query_response = exec_query(sp, (o,), database=database)
                    # input(query_response)

                    if len(query_response) > 0:
                        order_type = query_response[0]['tipodocto']
                        primary_number = query_response[0]['doctoerp']
                        secondary_number = query_response[0]['numpedido']

                        # Crea una orden de despacho que es un numero consecutivo. Con respecto a este número se hace el picking
                        # @planActual_resp:(MODELO) Plan actual utilizado para organizar los picking hechos cada cierto tiempo con planeación futura
                        # @op_resp: es el número de la orden de despacho
                        # t_seriepedido: Aqui queda la orden de despacho
                        sp = '''SET NOCOUNT ON
                                DECLARE @planActual_resp int, @op_resp int
                                    EXEC [web].[spI_AddNewOrdenDeDespacho] 
                                                        @bodega=%s,
                                                        @planActual=@planActual_resp output, 
                                                        @op=@op_resp output
                                select @planActual_resp planActual, @op_resp op '''
                        # Query que se hace directamente a la base de datos
                        try:
                            query_response = exec_query(
                                sp, (warehouse_code,), database=database)
                        except Exception as e:
                            print("Server Error!: ", e)
                            return JsonResponse({"message" : str(e)}, safe=False, status=500)

                        # Recuperamos el numero de la orden en la variable orden
                        order = query_response[0]['op']
                        response.append({'order': order, 'order_type': order_type, 'primary_number': primary_number,
                                        'secondary_number': secondary_number, 'origin_picking': o})
                        # input(response)

                        ''' 
                        El siguiente procedimiento va a insertar en la tabla t_materiales_por_orden.
                        @oden: es el número de la orden de despacho
                        @material: doctoERP
                        @color: tipoDocto
                        @eaninsumo: numpedido
                        @bodegareserva: bodega
                        Dentro de esa tabla se inserta el pedido que será despachado
                        '''
                        sp = '''SET NOCOUNT ON
                                EXEC [web].[spI_T_materiales_por_orden_Customized_Despacho] 
                                        @orden=%s, 
                                        @material=%s, 
                                        @color=%s , 
                                        @thypo='Orden de despacho', 
                                        @clase_consumo='ID', 
                                        @eaninsumo=%s, 
                                        @bodegareserva=%s, 
                                        @Descripcion='Pedido a despachar' '''
                        # Query que se hace directamente a la base de datos
                        try:
                            query_response = exec_query(
                                sp, (order, primary_number, order_type, secondary_number, warehouse_code), database=database)
                            # input(query_response)
                        except Exception as e:
                            if str(e) == "404":
                                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
                            else:
                                print("Server Error!: ", e)
                                return JsonResponse({"message" : str(e)}, safe=False, status=400)
                    else:
                        return JsonResponse([], safe=False, status=200)

                except Exception as e:
                    if str(e) == "404":
                        return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
                    else:
                        print("Server Error!: ", e)
                        return JsonResponse({"message" : str(e)}, safe=False, status=400)
            return JsonResponse(response, safe=False, status=200)
        elif picking_model == 'batch':
            # Crea una orden de despacho que es un numero consecutivo. Con respecto a este número se hace el picking
            # @planActual_resp:(MODELO) Plan actual utilizado para organizar los picking hechos cada cierto tiempo con planeación futura
            # @op_resp: es el número de la orden de despacho
            # t_seriepedido: Aqui queda la orden de despacho
            sp = '''SET NOCOUNT ON
                    DECLARE @planActual_resp int, @op_resp int
                        EXEC [web].[spI_AddNewOrdenDeDespacho] 
                                        @bodega=%s, 
                                        @planActual=@planActual_resp output, 
                                        @op=@op_resp output
                    select @planActual_resp planActual, @op_resp op '''
            # Query que se hace directamente a la base de datos
            try:
                query_response = exec_query(
                    sp, (warehouse_code,), database=database)
            except Exception as e:
                if str(e) == "404":
                    return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
                else:
                    return JsonResponse({"message" : str(e)}, safe=False, status=400)

            order = query_response[0]['op']
            for o in origin_picking:
                
                if str(plan_type) == "10":
                    sp = 'select tipodocto, doctoerp, numpedido from v_wms_epk where picking=%s'
                
                elif str(plan_type) == "11":
                    sp = 'select tipodocto, doctoerp, numpedido from v_wms_epn where picking=%s'

                else:
                    return JsonResponse({"message" : 'plan type is invalid'}, safe=False, status=400)

                # Query que se hace directamente a la base de datos
                try:
                    query_response = exec_query(sp, (o,), database=database)
                    if(len(query_response) == 0):
                        return JsonResponse([], safe=False, status=200)
                except Exception as e:
                    if str(e) == "404":
                        return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
                    else:
                        return JsonResponse({"message" : str(e)}, safe=False, status=400)

                order_type = query_response[0]['tipodocto']
                primary_number = query_response[0]['doctoerp']
                secondary_number = query_response[0]['numpedido']
                response.append({'order': order, 'order_type': order_type, 'primary_number': primary_number,
                                'secondary_number': secondary_number, 'origin_picking': o})

                sp = '''SET NOCOUNT ON
                        EXEC [web].[spI_T_materiales_por_orden_Customized_Despacho] 
                                @orden=%s, 
                                @material=%s, 
                                @color=%s , 
                                @eaninsumo=%s, 
                                @thypo='Orden de despacho', 
                                @clase_consumo='ID', 
                                @bodegareserva=%s, 
                                @Descripcion='Pedido a despachar' '''
                # Query que se hace directamente a la base de datos
                try:
                    query_response = exec_query(
                        sp, (order, primary_number, order_type, secondary_number, warehouse_code), database=database)
                except Exception as e:
                    if str(e) == "404":
                        return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
                    else:
                        return JsonResponse({"message" : str(e)}, safe=False, status=400)

            return JsonResponse(response, safe=False, status=200)

        elif picking_model == 'Picking load':
            return JsonResponse("falta", safe=False, status=200)

    return JsonResponse("Method doesn't exists", safe=False, status=400)
