import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from BackendApp.functions.plantillas.create import create_from_plantilla

from .epk import *
from .prv import *
from .euk_duk import *


@csrf_exempt
def import_csv(request):
    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':
        try:

            table = list(request_data.keys())[0]
            table_list = table.replace("'", '')
            table_list = table_list.split('-')

            for t in table_list:
                print(t)
                try:
                    print(database)
                    plantilla = list(request_data[str(table)].keys())[0]
                    print(plantilla)

                    data = request_data[str(table)][str(plantilla)]

                except Exception as e:
                    print(e)
                    print(e.__cause__)
                    return JsonResponse({'response': str(e)}, status=400)

                print("CREATING " + str(t) + " " + str(plantilla))
                response = create_from_plantilla(database, t, plantilla, data)

                if len(response['error']) > 0:
                    print(response['error'])
                    return JsonResponse(response, status=406)

            if len(response['lines']) > 0:
                return JsonResponse(response, status=200)
            else:
                return JsonResponse(response, status=400)

        except Exception as e:
            print(e)
            return JsonResponse({'response': str(e)}, status=400)
