from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BackendApp.utils import *


@csrf_exempt
def warehouses(request, warehouse_code=''):
    # Obtener datos del request
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']

    #del request_data['database']

    # Valida el metodo
    if request.method == 'GET':

        database_name = request.GET['database_name'] if 'database_name' in request.GET else None
        # warehouse_code = request_data["warehouse_code"] if "warehouse_code" in request_data else warehouse_code
        # Obtiene los parámetros del request y los cambia de diccionario a string
        where_param = None
        if "where" in request_data:
            where_param = " ".join(
                [d + " = '" + request_data["where"][d] + "' AND " for d in request_data['where'].keys()])
            where_param = where_param[:-4]

        response = []
        # Query que se hace directamente a la base de datos
        if warehouse_code == '':
            try:
                # database = request_data['database']
                # print(database)
                query = f"Select bodega, descripcion from t_ins_bodega" + \
                    (f" WHERE {where_param}" if where_param else "")

                if database_name:
                    response = exec_query(query, database=database_name)
                else:                   
                    response = exec_query(query, database=database)
            except Exception as e:
                print(e)
                return JsonResponse('Server Error: '+str(e), safe=False, status=500)
        else:
            try:
                query = "Select bodega, descripcion from t_ins_bodega where bodega = '" + \
                    warehouse_code + "'"
                response = exec_query(query, database=database)
            except Exception as e:
                print(e)
                return JsonResponse('Server Error: '+str(e), safe=False, status=500)

        # Conversion de la respuesta al formato que recibe el front
        if len(response) > 0:
            response = [{'warehouse_code': r["bodega"],
                        'warehouse_description': r["descripcion"]}
                        for r in response]

        return JsonResponse(response, safe=False, status=200)

    if request.method == 'POST':
        # print (request_data)

        response = []
        # Query que se hace directamente a la base de datos
        if not request_data:
            return JsonResponse('Body is required', safe=False, status=400)

        keys = " ".join([d+", " for d in request_data.keys()])
        keys = keys[0:-2]
        values = " ".join(
            ["'" + request_data[d] + "', " for d in request_data.keys()])
        values = values[0:-2]

        try:
            query = f"""INSERT INTO [dbo].[t_ins_bodega] ({keys}) VALUES ({values}) """
            exec_query(query, database=database)
        except Exception as e:
            return JsonResponse('Server Error: '+str(e), safe=False, status=500)

        try:
            query = "Select bodega, descripcion from t_ins_bodega where bodega = '" + \
                request_data["bodega"] + "'"
            response = exec_query(query, database=database)
        except Exception as e:
            return JsonResponse('Server Error: '+str(e), safe=False, status=500)

        # Conversion de la respuesta al formato que recibe el front
        if len(response) > 0:
            response = [{'warehouse_code': r["bodega"],
                        'warehouse_description': r["descripcion"]}
                        for r in response]

        return JsonResponse(response, safe=False, status=200)

    if request.method == 'PUT':
        response = []
        # Query que se hace directamente a la base de datos
        if "set" not in request_data:
            return JsonResponse('Set is required', safe=False, status=500)
        set_param = " ".join([d + " = '" + request_data['set']
                             [d] + "' , " for d in request_data['set'].keys()])
        set_param = set_param[:-2]

        where_param = None
        if "where" in request_data:
            where_param = " ".join(
                [d + " = '" + request_data["where"][d] + "' AND " for d in request_data['where'].keys()])
            where_param = where_param[:-4]

        try:
            query = f'''UPDATE [dbo].[t_ins_bodega] SET {set_param}''' + (
                f" WHERE {where_param}" if where_param else "")
            exec_query(query, database=database)
        except Exception as e:
            return JsonResponse('Server Error: '+str(e), safe=False, status=500)

        try:
            query = f"Select bodega, descripcion from t_ins_bodega" + \
                (f" WHERE {where_param}" if where_param else "")
            response = exec_query(query, database=database)
        except Exception as e:
            return JsonResponse('Server Error: '+str(e), safe=False, status=500)

        # Conversion de la respuesta al formato que recibe el front
        if len(response) > 0:
            response = [{'warehouse_code': r["bodega"],
                        'warehouse_description': r["descripcion"]}
                        for r in response]

        return JsonResponse(response, safe=False, status=200)

    if request.method == 'DELETE':
        response = []
        # Query que se hace directamente a la base de datos
        where_param = None
        if "where" in request_data:
            where_param = " ".join(
                [d + " = '" + request_data["where"][d] + "' AND " for d in request_data['where'].keys()])
            where_param = where_param[:-4]

        try:
            query = f"Select bodega, descripcion from t_ins_bodega" + \
                (f" WHERE {where_param}" if where_param else "")
            response = exec_query(query, database=database)
        except Exception as e:
            return JsonResponse('Server Error: '+str(e), safe=False, status=500)

        try:
            query = f'''delete from [dbo].[t_ins_bodega]''' + \
                (f" WHERE {where_param}" if where_param else "")
            exec_query(query, database=database)
        except Exception as e:
            return JsonResponse('Server Error: '+str(e), safe=False, status=500)

        # Conversion de la respuesta al formato que recibe el front
        if len(response) > 0:
            response = [{'warehouse_code': r["bodega"],
                        'warehouse_description': r["descripcion"]}
                        for r in response]

        return JsonResponse(response, safe=False, status=200)

    return JsonResponse("Method doesn't exists", safe=False, status=400)


def create_warehouses(warehouse):
    if "warehouse_code" not in warehouse:
        return '0', 'Warehouse code must be in the object'
    try:
        query = """SET NOCOUNT ON
                Insert into t_ins_bodega (Bodega, Descripcion, UbicacionF_C)
                Values ('"""+warehouse["warehouse_code"]+"""','"""+warehouse["description"]+"""','"""+warehouse["location"]+"""')"""
        exec_query(query=query)
        return '1', ''
    except Exception as e:
        return '0', str(e)
