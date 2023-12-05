
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def seguimiento_detallepicking(request):
    # try:
    #     request_data = JSONParser().parse(request)
    # except:
    #     request_data = {}

    request_data = request._body
    database = request_data['database']
    # request.GET
    if request.method == 'GET':
        numPicking = request.GET["numPicking"] if "numPicking" in request.GET else ''
        IsSoloPendientes = request.GET["IsSoloPendientes"] if "IsSoloPendientes" in request.GET else 0

        response = []
        sp = '''
            SET NOCOUNT ON
            EXEC [web].[usp_ObtenerProductosPicking_RCT]  %s, %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(
                sp, (numPicking, IsSoloPendientes,), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

            # print (sp)
        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
