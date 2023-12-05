
from urllib import request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from datetime import date
from ...utils import *

# CARGAMOS LA TABLA DE PLAN DESPACHOS


@csrf_exempt
def picking(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']
    role = request_data['role']
    id_employee = request_data['id_employee']

    endpoint = request.get_full_path()
    endpoint = endpoint.split('?')
    endpoint = str(request.method) + ' ' + str(endpoint[0])

    if request.method == 'GET':
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        fecha_inicial = request.GET["fecha_inicial"] if "fecha_inicial" in request.GET else None
        fecha = request.GET["fecha"] if "fecha" in request.GET else None
        fecha_final = request.GET["fecha_final"] if "fecha_final" in request.GET else None
        metodo = request.GET["metodo"] if "metodo" in request.GET else 0
        parametro = request.GET["parametro"] if "parametro" in request.GET else None
        tipodeplaneacion = request.GET["tipodeplaneacion"] if "tipodeplaneacion" in request.GET else 0
        tipodocto = request.GET["tipodocto"] if "tipodocto" in request.GET else None
        id_customer = request_data['id_customer'] if "id_customer" in request_data else ''


        response = []

        if role == 'customer':
            sp = '''SET NOCOUNT ON
            EXEC [web].[usp_ObtenerTblPlanDespachos_RCT_customer] %s, %s, %s, %s, %s, %s, %s, %s'''
        else:

            sp = '''SET NOCOUNT ON
                EXEC [web].[usp_ObtenerTblPlanDespachos_RCT] %s, %s, %s, %s, %s, %s, %s, %s'''

        # Query que se hace directamente a la base de datos
        if fecha is not None:
            fecha = fecha.replace("-", "")
        try:
            response = exec_query(
                sp, (bodega, fecha_inicial, metodo, parametro, tipodeplaneacion, tipodocto, fecha_final, id_customer), database=database, endpoint=endpoint)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
      

# Planeaaar
    if request.method == 'POST':
        # numero de orden de despacho generado anteriormente
        picking_order = request_data["picking_order"] if "picking_order" in request_data else [
        ]

        # Numero de bodega
        warehouse_code = request_data["warehouse_code"] if "warehouse_code" in request_data else ''

        # Empacador
        user = request_data["user"] if "user" in request_data and request_data["user"] != '' else None

        # Notas
        notes = request_data["notes"] if "notes" in request_data and request_data["notes"] != '' else None

        # Tipo de planeacion EPK(10) o EPN(11)
        plan_type = request_data["plan_type"] if "plan_type" in request_data and request_data["plan_type"] != '' else None
        cargue = request_data["cargue"] if "cargue" in request_data and request_data["cargue"] != '' else None
        validity = request_data["validity"] if "validity" in request_data and request_data["validity"] != '' else None
        # fecha = request_data["fecha"] if "fecha" in request_data and request_data["fecha"] != '' else None
        fecha_inicial = request_data["fecha_inicial"] if "fecha_inicial" in request_data and request_data["fecha_inicial"] != '' else None
        fecha_final = request_data["fecha_final"] if "fecha_final" in request_data and request_data["fecha_final"] != '' else None
        picking_order = set(picking_order)
        response = []

        if fecha_inicial is not None:
            fecha_inicial = fecha_inicial.replace("-", "")


        if fecha_final is not None:
            fecha_final = fecha_final.replace("-", "")

        for p in picking_order:
            # input(p)
            sp = '''EXEC [web].[usp_wms_GetDetallePrepack_Fast_RCT] 
                            @ordenDespacho=%s, 
                            @bod=%s, 
                            @npedid = %s,
                            @empacador=%s, 
                            @observaciones=%s, 
                            @tipoplaneacion=%s, 
                            @cargue=%s,
                            @Meses=%s
                    '''

            try:
                query_response = exec_query(
                    sp, (p, warehouse_code, None, id_employee, notes, plan_type, cargue, validity), database=database)

                # today = date.today()
                # format_today = date.today().strftime("%Y%m%d")
            except Exception as e:
                print("Server Error!: ", e)
                return JsonResponse({"message" : str(e)}, safe=False, status=500)

        try:
            if str(plan_type) == '10':
                sp = f'''select *, ISNULL(f.Valida,0) as EstadoPicking FROM [ufn_obtenertblplandespachos_epk_ext_allcompany_RCT] ('{fecha_inicial}', '{warehouse_code}','{fecha_final}')f where f.OrdenDespacho in ({str(picking_order)[1:-1]})'''
            else:
                sp = f'''select *, ISNULL(f.Valida,0) as EstadoPicking FROM [ufn_obtenertblplandespachos_epn_ext_allcompany_RCT] ('{fecha_inicial}', '{warehouse_code}','{fecha_final}')f where f.OrdenDespacho in ({str(picking_order)[1:-1]})'''
            # sp = f'''select *, ISNULL(f.Valida,0) as EstadoPicking FROM [web].[ufn_obtenertblplandespachos_epk_ext_allcompany_RCTxOrdenDespacho] ('{warehouse_code}','{str(picking_order)[1:-1]}') f'''
            query_response = exec_query(sp, database=database)
            print(query_response)
            response.extend(query_response)    
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse({"message" : str(e)}, safe=False, status=500)

        print("The length of the response is " + str(len(response)))
        return JsonResponse(response, safe=False, status=200)


# ACTUALIZAR UN CAMPO DE DESCRIPCIONES
  # ACTUALIZAR UN CAMPO DE DESCRIPCIONES
    if request.method == 'DELETE':

        # id = request.GET["id"] if "id" in request.GET else ''
        plan_type = request_data["plan_type"] if "plan_type" in request_data else None
        picking = request_data["picking"] if "picking" in request_data else None
        pickingerp = request_data["pickingERP"] if "pickingERP" in request_data else None
        # fecha = request_data["fecha"] if "fecha" in request_data and request_data["fecha"] != '' else None
        fecha_inicial = request_data["fecha_inicial"] if "fecha_inicial" in request_data and request_data["fecha_inicial"] != '' else None
        fecha_final = request_data["fecha_final"] if "fecha_final" in request_data and request_data["fecha_final"] != '' else None
        bodega = request_data["bodega"] if "bodega" in request_data and request_data["bodega"] != '' else None
        EstadoPicking = request_data["EstadoPicking"] if "EstadoPicking" in request_data and request_data["EstadoPicking"] != '' else None

        if picking is None or pickingerp is None:
            return JsonResponse({"message": "No se ha enviado el picking"}, safe=False, status=400)

        if plan_type is None:
            return JsonResponse({"message": "No se ha enviado el tipo de planeacion"}, safe=False, status=400)
        
        if int(EstadoPicking) == 3:
        # Se agrega el item a la lista
            sp = '''SET NOCOUNT ON
                    EXEC [web].[usp_EliminarPicking_RCT] %s '''

            # Query que se hace directamente a la base de datos
            try:

                response = exec_query(sp, (picking,), database=database)
                # Se Muestran los item correspondientes a todo el grupo
                # sp = ''' SET NOCOUNT ON
                #      EXEC [web].[spS_T_ins_descripcionesxGrupo] %s'''

                # Returns the response

                try:
                    if str(plan_type) == '10':
                        sp = f'''select *, ISNULL(f.Valida,0) as EstadoPicking FROM [ufn_obtenertblplandespachos_epk_ext_allcompany_RCT] ('{fecha_inicial}', '{bodega}', '{fecha_final}')f where f.pickingerp in ({pickingerp})'''
                    else:
                        sp = f'''select *, ISNULL(f.Valida,0) as EstadoPicking FROM [ufn_obtenertblplandespachos_epn_ext_allcompany_RCT] ('{fecha_inicial}', '{bodega}', '{fecha_final}')f where f.pickingerp in ({pickingerp})'''       
                    query_response = exec_query(sp, database=database)
                    print(query_response)  
                    return JsonResponse(query_response, safe=False, status=200)
                except Exception as e:
                    print("Server Error!: ", e)
                    return JsonResponse({"message" : str(e)}, safe=False, status=500)


            except Exception as e:
                print("Server Error!: ", e)
                return JsonResponse({"message" : str(e)}, safe=False, status=500)
            
        elif int(EstadoPicking) == 0:


            sp = '''SET NOCOUNT ON
                    EXEC [web].[eliminar_pedidoxPicking] %s '''
            
            try:
                response = exec_query(sp, (pickingerp,), database=database)
                print(response) 
                return JsonResponse({"message" : "Eliminado correctamente"}, safe=False, status=200)
            except Exception as e:
                print("Server Error!: ", e)
                return JsonResponse({"message" : str(e)}, safe=False, status=500)

        else:
            return JsonResponse({"message": "No se puede eliminar el picking"}, safe=False, status=400)