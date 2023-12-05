from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from BackendApp.models import *
from siesa.models import *


@csrf_exempt
def T121Mc(request):

    request_data = request._body
    database = request_data['database'] + '_siesa'

    if request.method == 'GET':
            
            table = T121McItemsExtensiones.objects.using(database).all()
            table = list(table.values())

            return JsonResponse(table, safe=False, status=200)

