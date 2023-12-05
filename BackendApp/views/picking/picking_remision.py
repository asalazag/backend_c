from copy import deepcopy
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from wmsAdapter.models import TdaWmsEpk

from BackendApp.utils import *


@csrf_exempt
def picking_remision(request):
    '''
    Esta vista se encarga de obtener el siguiente numero de remisión que será tomado la secuencia cargue de la base de datos y 
    almacenado en el campo cargue de TDA_WMS_EPK
    '''

    # Se obtiene el body del request
    request_data = request._body

    # Se obtiene el nombre de la base de datos
    database = request_data['database']
    database_adapter = database + '_adapter'

    # Metodo GET
    if request.method == 'GET':

        

        # Declare array response
        response = []

        # get the variables from the request
        picking = request.GET.get('picking', None)
        doctoerp = request.GET.get('doctoerp', None)
        numpedido = request.GET.get('numpedido', None)

        # Validate if there is a cargue depending on the picking, doctoerp and numpedido
        cargue = list(TdaWmsEpk.objects.using(database_adapter).filter(
            picking=picking, doctoerp=doctoerp, numpedido=numpedido).values('cargue'))
        
        # If there is a cargue, return the cargue
        if cargue[0]['cargue'] is not None and cargue[0]['cargue'] != '':
            # Validate if cargue is associated to 2 or more pickings
            validate_cargue = list(TdaWmsEpk.objects.using(database_adapter).filter(
                cargue=cargue[0]['cargue']).values('picking'))
            
            # If there are 2 or more pickings associated to the cargue, return an error
            if len(validate_cargue) > 1:
                return JsonResponse({"message" : 'Cargue asociado a 2 o mas picking'}, safe=False, status=406)

            # If there is only one picking associated to the cargue, return the cargue
            else:
                return JsonResponse(cargue, safe=False, status=200)
            
        # If there is not a cargue, return the next cargue
        else:

            # Se obtiene el siguiente numero de remisión
            sp = '''SET NOCOUNT ON
                select next value for secuencia_cargue as cargue'''

            # Query que se hace directamente a la base de datos
            try:
                response = exec_query(
                    sp, (), database=database)
                print("The length of the response is " + str(len(response)))

                # save the cargue in the database
                TdaWmsEpk.objects.using(database_adapter).filter(
                    picking=picking, doctoerp=doctoerp, numpedido=numpedido).update(cargue=response[0]['cargue'])

                # convert the cargue to string
                response[0]['cargue'] = str(response[0]['cargue'])

                # Returns the response
                return JsonResponse(response, safe=False, status=200)
            except Exception as e:
                if str(e) == "404":
                    return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
                else:
                    return JsonResponse({"message" : str(e)}, safe=False, status=400)
