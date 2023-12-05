from ctypes import c_double, c_int
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *


@csrf_exempt
def images_url(request):

    request_data = request._body
    database = request_data['database']


#  CONSULTAMOS LAS REFERENCIAS EXISTENTES EN LA TABLA (T_Detalle_referencia_CV) DE CONTROL DE VIGENCIAS DE UNA BODEGA INDICADA
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        
        productoEAN = request.GET["productoEAN"] if "productoEAN" in request.GET else ''
        bodega = request.GET["bodega"] if "bodega" in request.GET else ''
        
        if productoEAN == '':
            return JsonResponse({"message" : 'Debe ingresar un producto'}, safe=False, status=400)
        if bodega == '':
            return JsonResponse({"message" :'Debe ingresar una bodega valida'}, safe=False, status=400)
        
        response = []
        sp = ''' SET NOCOUNT ON
             select cv.imageurl from t_detalle_refencia_CV cv
                where cv.productoEAN = %s and cv.bodega = %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (productoEAN,bodega,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Items not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)


# ADICIONA UN REGISTRO DE ZONAS POR EMPLEADO
    if request.method == 'PUT':

        # id = request.GET["id"] if "id" in request.GET else ''
        bodega = request_data["bodega"] if "bodega" in request_data else ''
        productoEAN = request_data["productoEAN"] if "productoEAN" in request_data else ''
        url = request_data["url"] if "url" in request_data else ''
        
        
        if productoEAN == '':
            return JsonResponse({"message" : 'Debe ingresar un producto'}, safe=False, status=400)
        if url == '':
            return JsonResponse({"message" :'Debe ingresar una imagen de producto'}, safe=False, status=400)
        if bodega == '':
            return JsonResponse({"message" :'Debe ingresar una bodega valida'}, safe=False, status=400)
        
        
        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
            declare @imageurl varchar(max) = %s
            declare @productoEAN varchar(100) = %s
            declare @bodega varchar(20) =  %s
                update cv
                set cv.imageurl = @imageurl
                from t_detalle_refencia_CV cv
                where cv.productoEAN = @productoEAN and cv.bodega = @bodega;
                select cv.imageurl from t_detalle_refencia_CV cv
                where cv.productoEAN = @productoEAN and cv.bodega = @bodega;'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp,
                                  (url,productoEAN,bodega,), database=database)

            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            if str(e) == "404":
                return JsonResponse({"message" : 'Item not fount'}, safe=False, status=404)
            else:
                return JsonResponse({"message" : str(e)}, safe=False, status=400)

