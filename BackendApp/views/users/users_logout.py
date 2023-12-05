from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from BackendApp.models import *

from ...utils import *


@csrf_exempt
def users_logout(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':

        empleado = request_data["empleado"] if "empleado" in request_data else None

        if empleado == None:
            return JsonResponse('Ingrese un empleado valido', safe=False, status=400)
        response = []
        sp = '''
             Update dbo.t_ins_descripciones set descripcion=1 where grupo='_userstatus' and codigodescripcion= %s;
             select 'Ok' as mensaje
             '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (empleado,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            print("Server Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)


