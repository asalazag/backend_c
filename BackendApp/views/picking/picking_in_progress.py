
from array import array
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connections


from ...utils import *


@csrf_exempt
def get_picking_in_progress(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    warehouse = request_data['warehouse']
    database = request_data['database']
    id_customer = request_data['id_customer'] if "id_customer" in request_data else ''

    if request.method == 'GET':

        if not warehouse or warehouse == '':
            warehouse = None
            
        sp = '''

                SET NOCOUNT ON
                EXEC [web].[usp_ShowCardPicking]  %s, %s
                '''
        try:

            response = exec_query(
                sp, (str(warehouse),str(id_customer),), database=database)
            
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)

            
