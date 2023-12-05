from urllib import response
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from BackendApp.utils import exec_query

'''
This view is to view the fields of a sp and
'''
@csrf_exempt
def random_queries(request): 
    request_data = request._body  # Gets the body of the request
    database = request_data['database'] # Gets the database
    request_data.pop('database') # Removes the database from the request
    request_data.pop('id_employee')
    request_data.pop('warehouse') # Removes the id_employee from the request
    request_data.pop('id_customer')
    request_data.pop('role')

   #This view is used to get the fields of a Table or of an Store Procedure
    if request.method == 'GET': # If the request is a GET

        codSelec      = request.GET["codSelec"]      if "codSelec" in request.GET else None # Gets the data sent in the body of the request
        ReturnXML     = request.GET["ReturnXML"]     if "ReturnXML" in request.GET else 0 # Gets the data sent in the body of the request
        criterio_busq = request.GET["criterio_busq"] if "criterio_busq" in request.GET else None # Gets the data sent in the body of the request        

        sp = '''SET NOCOUNT ON
        EXEC [web].[spS_T_ins_Consultas_Aleatorias] 
                @codSelec=%s, @ReturnXML=%s, @criterio_busq=%s  '''  # Store Procedure
        response = []
        sp = '[web].[spS_T_ins_Consultas_Aleatorias] %s ,%s ,%s'

        
        try: # Try to execute the query
            # print (sp)
            response = exec_query(query = sp, params=(codSelec, ReturnXML, criterio_busq), database=str(database)) # Executes the query
            # print (response)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e: # If the query fails
            print("Server Error!: ", e) # Prints the error
            return JsonResponse('There was a problem executing the request', safe=False, status=500) # Returns an error
        
        return JsonResponse(response, safe=False, status=200) # Returns the response