""" Dependencies"""
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

""" Functions """
from BackendApp.functions.api.DynamicQueries.dynamic_queries import execute_dynamic_queries

@csrf_exempt
def dynamic_queries_execute_view(request):
    '''
    Dynamic queries view to execute
    '''

    request_data = request._body
    
    database = request_data['database']

#  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'GET':
        try:
            # Declare params
            params = {}

            # Get params
            id_param = request.GET.get('id', None)
            codigo = request.GET.get('codigo', None)

            # create params
            if id_param:
                params['id'] = id_param
            
            if codigo:
                params['codigo'] = codigo

            # Get response
            response = execute_dynamic_queries(database, params)

            # Print response
            print(response.json())

            # Return response
            return JsonResponse(response.json(), safe=False, status=response.status_code)
        
        # excepting error
        except Exception as e:
            print (str(e))
            return JsonResponse({'message' : str(e)}, safe=False, status=500)
          
    