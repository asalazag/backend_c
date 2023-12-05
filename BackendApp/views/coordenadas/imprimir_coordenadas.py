from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def imprimir_coordenadas(request):

    request_data = request._body
    database = request_data['database']
    idempleado = request_data['id_employee']
    warehouse = request_data['warehouse']

    # Imprimir coordenadas
    if request.method == 'POST':
        
        bodega = request_data["bodega"] if "bodega" in request_data else ''
        pasillo = request_data["pasillo"] if "pasillo" in request_data else 0
        lado = request_data["lado"] if "lado" in request_data else 0
        mueble_inicia = request_data["mueble_inicia"] if "mueble_inicia" in request_data else 0
        mueble_finaliza = request_data["mueble_finaliza"] if "mueble_finaliza" in request_data else 0
        piso_inicia = request_data["piso_inicia"] if "piso_inicia" in request_data else 0
        piso_finaliza = request_data["piso_finaliza"] if "piso_finaliza" in request_data else 0
        genera_rotulo = request_data["genera_rotulo"] if "genera_rotulo" in request_data else 0
        impresora = request_data["impresora"] if "impresora" in request_data else 0
        rotulo = request_data["rotulo"] if "rotulo" in request_data else 2
    
        response = []

        print("pasillo: ", pasillo)

        # Se agrega el item a
        sp = '''SET NOCOUNT ON
                    EXEC [web].[usp_tmpCargaInvInicial_ZPL_SMT_FULL_app] %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (bodega,pasillo,lado,mueble_inicia,mueble_finaliza,piso_inicia,piso_finaliza,idempleado,genera_rotulo,impresora,rotulo,), database=database)

            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

