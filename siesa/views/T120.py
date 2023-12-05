from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from BackendApp.models import *
from siesa.models import *


@csrf_exempt
def T120(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'GET':
        try:
            registros = T120McItems.objects.using(database).all()
            return JsonResponse(registros, safe=False, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Error getting T120McItems'}, safe=False, status=500)

