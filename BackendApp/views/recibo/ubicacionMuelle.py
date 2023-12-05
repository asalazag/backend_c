from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def muelleUbicacionBodega(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAMOS LOS MUELLES
    if request.method == 'GET':

        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        
        response = []
        sp = ''' SET NOCOUNT ON
                 select ubicación from T_Ins_Coordenadas where ubicación like %s and bodegac = %s'''
        
        try:
            response = exec_query(sp, ('%MU%',bodega,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
       
        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)


# ADICIONA EL REGISTRO SANITARIO
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega = request_data["bodega"] if "bodega" in request_data else None
        muelle = request_data["muelle"] if "muelle" in request_data else None
               
        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [dbo].[usp_creaUbicacionMuelle] %s, %s
         '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,(bodega,muelle,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        
        except Exception as e:
            print("Server Error!: ", e)

            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)
            

# ELIMINA UNA UBICACION DE MUELLE
    if request.method == 'DELETE':

        # print (request.method);

        muelle = request.GET["muelle"] if "muelle" in request.GET else ''
        
        response = []

        # Query que se hace directamente a la base de datos
        sp = '''SET NOCOUNT ON
                delete  from T_Ins_Coordenadas where ubicación = %s
                '''
        try:

            response = exec_query(sp, (muelle,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            if str(e) == "404":
                return JsonResponse({"message" : 'not found'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=500)
