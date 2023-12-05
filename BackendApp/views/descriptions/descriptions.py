from typing import Any
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ...utils import *
        
@csrf_exempt
def descriptions(request): 

    request_data = request._body
    database = request_data['database']

#  CONSULTAR UN EMPLEADO
    if request.method == 'GET':

        # id = request.GET["id"] if "id" in request.GET else ''
        Grupo =request.GET ["grupo"] if "grupo" in request.GET else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spS_T_ins_descripciones] %s'''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (Grupo,), database=database)
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

#ACTUALIZAR UN CAMPO DE DESCRIPCIONES
    if request.method == 'POST':
  
        # id = request.GET["id"] if "id" in request.GET else ''
        Grupo = request_data["Grupo"] if "Grupo" in request_data else ''
        CodigoDescripcion = request_data["CodigoDescripcion"] if "CodigoDescripcion" in request_data else ''
        Descripcion  = request_data["Descripcion"]  if "Descripcion"  in request_data else ''


        response = []


        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spI_T_ins_Descripciones] %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (Grupo,CodigoDescripcion,Descripcion), database=database)
            #Se Muestran los item correspondientes a todo el grupo
            sp = ''' SET NOCOUNT ON
                 EXEC [web].[spS_T_ins_descripcionesxGrupo] %s'''

            response = exec_query(sp, (Grupo,), database=database)   

            return JsonResponse(response, safe=False, status=200) # Returns the response

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

#ACTUALIZAR UN CAMPO DE DESCRIPCIONES
    if request.method == 'DELETE':
  
        # id = request.GET["id"] if "id" in request.GET else ''
        Grupo = request_data["Grupo"] if "Grupo" in request_data else ''
        CodigoDescripcion = request_data["CodigoDescripcion"] if "CodigoDescripcion" in request_data else ''
        Descripcion  = request_data["Descripcion"]  if "Descripcion"  in request_data else ''


        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spD_T_ins_Descripciones] %s , %s , %s '''


        # Query que se hace directamente a la base de datos
        try:

            response = exec_query(sp, (Grupo,CodigoDescripcion,Descripcion), database=database)
            #Se Muestran los item correspondientes a todo el grupo
            sp = ''' SET NOCOUNT ON
                 EXEC [web].[spS_T_ins_descripcionesxGrupo] %s'''

            response = exec_query(sp, (Grupo,), database=database)   
            return JsonResponse(response, safe=False, status=200) # Returns the response

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)

#ACTUALIZAR UN CAMPO DE DESCRIPCIONES
    if request.method == 'PUT':
  
        # id = request.GET["id"] if "id" in request.GET else ''
        Grupo = request_data["Grupo"] if "Grupo" in request_data else ''
        CodigoDescripcion = request_data["CodigoDescripcion"] if "CodigoDescripcion" in request_data else ''
        Descripcion  = request_data["Descripcion"]  if "Descripcion"  in request_data else ''


        response = []


        # Se agrega el item a la lista
        sp = '''SET NOCOUNT ON
                EXEC [web].[spU_T_ins_Descripciones] %s , %s , %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (Grupo,CodigoDescripcion,Descripcion), database=database)
            #Se Muestran los item correspondientes a todo el grupo
            sp = ''' SET NOCOUNT ON
                 EXEC [web].[spS_T_ins_descripcionesxGrupo] %s'''

            response = exec_query(sp, (Grupo,), database=database)   
            return JsonResponse(response, safe=False, status=200) # Returns the response

        except Exception as e:
            return JsonResponse('Server Error!', safe=False, status=500)


