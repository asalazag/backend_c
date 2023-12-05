from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ...utils import *


@csrf_exempt
def lista_vigencias(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']

    if request.method == 'GET':
        # response = []
        sp = '''select distinct listavigencias as lista from dbo.t_detalle_refencia_CV'''
        try:
            response = exec_query(
                sp, database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
