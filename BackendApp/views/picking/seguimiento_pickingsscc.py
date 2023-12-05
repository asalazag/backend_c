from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def seguimiento_pickingsscc(request):
  # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']

    print(request_data)
    # request.GET
    if request.method == 'GET':
        numpicking = request.GET["numpicking"] if "numpicking" in request.GET else ''

        response = []
        sp = '''
            SET NOCOUNT ON
            EXEC [web].[usp_detalleSSCCxCaja_rct]  %s, '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (numpicking,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

            # print (sp)
        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
