from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests

from ...utils import *


@csrf_exempt
def zpl(request):
    request_data = request._body
#  CONSULTAR UNA LISTA DE ARTICULOS QUE COINCIDAN CON LA DESCRIPCION INDICADA
    if request.method == 'POST':
        try:
            response_json = {}
            try:
                zpl_code = request_data["data"] if "data" in request_data else None
                # print(zpl_code)
                if zpl_code is None:
                    return JsonResponse('No se ha indicado el codigo ZPL', safe=False, status=400)

                base_url = 'http://api.labelary.com/v1/printers/8dpmm/labels/4x6/0/'

                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/pdf'
                }

                response = requests.post(
                    base_url, data=zpl_code, headers=headers)

                retArray = [int(i) for i in response.content]

                response_json["data"] = retArray
                return JsonResponse(response_json, safe=False, status=200)
            except Exception as e:
                print("Server Error!: ", e)
                return JsonResponse('Server Error!', safe=False, status=500)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)
