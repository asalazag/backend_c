from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from settings.models import *
from BackendApp.functions.api import *

from ...utils import *


@csrf_exempt
def active_integrations(request):
    
        database = request.db_name


        if request.method == 'GET':
            try:
                apikey = get_apikey(database)
                print(apikey)

                

                return JsonResponse(apikey, safe=False, status=200)

            except:   
                return JsonResponse('Server Error!', safe=False, status=500)           
        
        