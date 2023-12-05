from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def descriptoreslogisticos(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAMOS LOS DESCRIPTORES LOGISTICOS DE UN LOTE
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        NumeroCaja        = request.GET["NumeroCaja"]       if "NumeroCaja"       in request.GET else 0
     
        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spS_LogisticasXCaja] %s ,'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,(NumeroCaja,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)


# ADICIONA LOS DESCRIPTORES CORRESPONDIENTES A UN LOTE
    if request.method == 'POST':

        # id = request.GET["id"] if "id" in request.GET else ''
        CajaNo = request_data["CajaNo"] if "CajaNo" in request_data else 0
        vbl1   = request_data["vbl1"]   if "vbl1"   in request_data else ''
        vbl2   = request_data["vbl2"]   if "vbl2"   in request_data else ''
        vbl3   = request_data["vbl3"]   if "vbl3"   in request_data else ''
        vbl4   = request_data["vbl4"]   if "vbl4"   in request_data else ''
        vbl5   = request_data["vbl5"]   if "vbl5"   in request_data else 0


        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spI_LogisticasXCaja] %s , %s , %s ,%s , %s, %s   '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (CajaNo, vbl1, vbl2, vbl3, vbl4, vbl5,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)



# ACTUALIZAR LA INFORMACION DE LOS DESCRIPTORES DE UN LOTE INDICADO
    if request.method == 'PUT':

        id     = request_data["id"]     if "id"      in request_data else 0
        CajaNo = request_data["CajaNo"] if "CajaNo"  in request_data else 0
        vbl1   = request_data["vbl1"]   if "vbl1"    in request_data else ''
        vbl2   = request_data["vbl2"]   if "vbl2"    in request_data else ''
        vbl3   = request_data["vbl3"]   if "vbl3"    in request_data else ''
        vbl4   = request_data["vbl4"]   if "vbl4"    in request_data else ''
        vbl5   = request_data["vbl5"]   if "vbl5"    in request_data else ''
 
        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spU_LogisticasXCaja]  %s , %s , %s ,%s , %s, %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (id, CajaNo, vbl1, vbl2, vbl3, vbl4, vbl5,), database=database)

            # Returns the response
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)


# ELIMINA LA INFORMACION DE LOS DESCRIPTORES DE UN LOTE
    if request.method == 'DELETE':

        # print (request.method);

        id = request_data["id"] if "id" in request_data else 0

        response = []

        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spD_LogisticasXCaja] %s '''

        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (id,), database=database)
            print("The length of the response is " + str(len(response)))
            # Returns the response
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

