import json
from urllib import response
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from BackendApp.utils import exec_query

'''
This view is to view the fields of a sp and
'''


@csrf_exempt
def dynamics(request):

    request_data = request._body  # Gets the body of the request
    database = request_data['database']  # Gets the database
    request_data.pop('database')  # Removes the database from the request
    request_data.pop('id_employee')
    request_data.pop('warehouse')  # Removes the id_employee from the request
    request_data.pop('id_customer')
    request_data.pop('role')  # Removes the id_customer from the request

   # This view is used to get the fields of a Table or of an Store Procedure
    if request.method == 'GET':  # If the request is a GET

        sp = ''' SET NOCOUNT ON
        EXEC [web].[spS_ObtenerCamposDeTabla] %s '''  # Store Procedure

        # Gets the data sent in the body of the request
        stored_procedure = request.GET['stored_procedure'] if 'stored_procedure' in request.GET else ''

        if stored_procedure == '':  # If the stored procedure is empty
            # Returns an error
            return JsonResponse("The stored procedure wasn't specified", safe=False, status=400)
        else:  # If the stored procedure is not empty
            try:  # Try to execute the query
                response = exec_query(query=sp, params=(
                    str(stored_procedure),), database=str(database))  # Executes the query
            except Exception as e:  # If the query fails
                # Returns an error
                return JsonResponse('There was a problem executing the request', safe=False, status=500)

        response_dict = {}  # Creates a list to store the data
        if len(response) > 0:  # If the query returns data

            for r in response:  # For each record in the response
                # Adds the field to the list
                response_dict[r["NombreCampo"]] = None
        # Returns the response
        return JsonResponse([response_dict], safe=False, status=200)

    if request.method == 'POST':  # If the request is a POST

        sp = ''' SET NOCOUNT ON
         EXEC [web].[spS_ObtenerCamposDeTabla] %s '''  # Store Procedure

        stored_procedure = request_data["stored_procedure"] if "stored_procedure" in request_data else ''
        if stored_procedure == '':  # If the stored procedure is empty
            # Returns an error
            return JsonResponse("The stored procedure wasn't specified", safe=False, status=400)
        else:  # If the stored procedure is not empty
            try:  # Try to execute the query
                fields = exec_query(query=sp, params=(
                    str(stored_procedure),), database=str(database))  # Executes the query

                fields_list = []  # Creates a list to store the data
                # print(fields)
                if len(fields) > 0:  # If the query returns data

                    for r in fields:  # For each record in the response
                        # Adds the field to the list
                        fields_list.append(r["NombreCampo"])

                # print(fields_list)
                # [0].replace('"', "'")
                fields_sp = request_data['fields_sp']
                # fields_sp = fields_sp[1:-1]
                # input(fields_sp)
                # fields_sp = json.loads(fields_sp)
                # print(fields_sp)

                sp = '''SET NOCOUNT ON
                     EXEC [dbo].[{}] '''.format(stored_procedure)  # Store Procedure

                args_list = []  # Creates a list to store the data
                for field in fields_list:  # For each field in the list
                    # Gets the data sent in the body of the request
                    args = fields_sp[field] if field in fields_sp else None
                    print(args)
                    # if args != None:  # If the data is not empty
                    args_list.append(args)  # Adds the data to the list
                    # else:  # If the data is empty
                    #     # Returns an error
                    #     return JsonResponse("The field " + field + " wasn't specified", safe=False, status=400)

                for i in range(len(args_list)):  # For each data in the list
                    sp += '%s,'  # Adds the data to the query
                sp = sp[:-1]  # Removes the last comma

                args_tuple = tuple(args_list)  # Creates a tuple with the data

                # sp = "'''SET NOCOUNT ON EXEC " + sp + "'''"
                # print(sp)
                # print(args_tuple)
                response = exec_query(query=sp, params=args_tuple, database=str(
                    database))  # Executes the query
                # response = exec_query(sp, args_tuple, str(database)) # Executes the query
                # response = response[0]
                # Returns the response
                return JsonResponse(response, safe=False, status=200)

            except Exception as e:  # If the query fails
                print("Server Error!: ", e)  # Prints the error
                # Returns an error
                return JsonResponse({"message" : str(e)}, safe=False, status=400)
