#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from django.db import connections
from django.conf import settings
from ...utils import *
from settings.models.config import config
from pymongo import MongoClient
import re
@csrf_exempt
def alter_update_procedures(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'PUT':

        origin = request_data["origin"] if "origin" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else None
        if origin is None:
            return JsonResponse({"message" : "origin is required"}, safe=False, status=405)
        elif destination is None:
            return JsonResponse({"message" : "destination is required"}, safe=False, status=405)
        try:
            list_sp_base = []
            list_sp_adapter = []
            if '_adapter' in origin:
                        adapter_origin = settings.DATABASES[origin]['NAME']
                        base = origin.split('_')[0]
                        base_origin = settings.DATABASES[base]['NAME']
                        adapter_destino = settings.DATABASES[destination]['NAME'] 
                        base2 = destination.split('_')[0]
                        base_destino = settings.DATABASES[base2]['NAME']
            else:
                base_destino = settings.DATABASES[destination]['NAME']
                adapter_destino = settings.DATABASES[destination+"_adapter"]['NAME']
                base_origin = settings.DATABASES[origin]['NAME']
                adapter_origin = settings.DATABASES[origin+"_adapter"]['NAME']
            
            origen_cursor  = connections[origin].cursor()
            querybase = f"EXEC [dbo].[dev_find_]'{base_origin}'"
            queryadapter = f"EXEC [dbo].[dev_find_]'{adapter_origin}'"    

            origen_cursor.execute(querybase)
            response = origen_cursor.fetchall()
            list_sp_base = [row[0] for row in response]
            # print ('list_sp_base______________________')
            # print(list_sp_base)

            origen_cursor.execute(queryadapter)
            response = origen_cursor.fetchall()
            list_sp_adapter = [row[0] for row in response]
            # print ('list_sp_adapter______________________')
            # print(list_sp_adapter)

            merged_list = list_sp_base.copy()
            merged_list.extend(list_sp_adapter)
            # print ('merged_list______________________')
            # print(merged_list)
            print(destination)
            # for sp_x in list_sp_base:
            #     print(sp_x + ' ----> ' + destination)
            #     sp_query = f"SELECT OBJECT_DEFINITION(OBJECT_ID('{sp_x}')) AS codigo_sp"
            #     origen_cursor.execute(sp_query)
            #     sp_codigo = origen_cursor.fetchone()[0]
            #     sp_codigo = sp_codigo.replace(str(base_origin),str(base_destino))
            #     sp_codigo = sp_codigo.replace(str(adapter_origin),str(adapter_destino))
            #     print(sp_codigo)
            errores = {}
            for sp_x in merged_list:
                try:
                    print(sp_x + ' ----> ' + destination)
                    sp_query = f"SELECT OBJECT_DEFINITION(OBJECT_ID('{sp_x}')) AS codigo_sp"
                    origen_cursor.execute(sp_query)
                    sp_codigo = origen_cursor.fetchone()[0]
                    if sp_codigo is None:
                        print(f"{sp_x} doesn't exist in origin database")
                        return JsonResponse({"message" : f"{sp_x} doesn't exist in origin database"}, safe=False, status=405)
                    
                    if '_adapter' in origin:
                        adapter_origin = settings.DATABASES[origin]['NAME']
                        base = origin.split('_')[0]
                        base_origin = settings.DATABASES[base]['NAME']
                        
                    else: 
                        base_origin = settings.DATABASES[origin]['NAME']
                        adapter_origin = settings.DATABASES[origin+"_adapter"]['NAME']
                    
                    if '_adapter' in destination:
                        adapter_destino = settings.DATABASES[destination]['NAME'] 
                        base = destination.split('_')[0]
                        base_destino = settings.DATABASES[base]['NAME']
                    else:
                        base_destino = settings.DATABASES[destination]['NAME']
                        adapter_destino = settings.DATABASES[destination+"_adapter"]['NAME']
                    

                    sp_codigo = sp_codigo.replace(str(base_origin),str(base_destino))
                    sp_codigo = sp_codigo.replace(str(adapter_origin),str(adapter_destino))
                    # print(sp_codigo)

                    try:
                        sp_codigoact = ""
                        sp_codigoactver = ""
                        sp_codigo = reemplazarfunction(sp_codigo)
                        sp_codigo = reemplazarprocedure(sp_codigo)
                        sp_codigo = reemplazarview(sp_codigo)
                        try:
                            destino_cursor  = connections[destination].cursor()
                            destino_cursor.execute(sp_query)
                            sp_codigoact = destino_cursor.fetchone()[0]
                            destino_cursor.close()
                            sp_codigoactver = reemplazarfunction(sp_codigoact)
                            sp_codigoactver = reemplazarprocedure(sp_codigoactver)
                            sp_codigoactver = reemplazarview(sp_codigoactver)
                        except Exception as e:
                            destino_cursor.close()
                            errores[destination] = str(e)
                        if sp_codigoactver == sp_codigo:
                            print(f"{sp_x} is the same in {destination} database")
                            continue
                        else:
                            destino_cursor  = connections[destination].cursor()                                                        
                            destino_cursor.execute(sp_codigo)
                            destino_cursor.close()
                            print(f"Objet created  in {destination}")
                            
                    except Exception as e:
                        errores[destination] = str(e)
                    
                except Exception as e:
                    print(e)
                    print(sp_x)
                    origen_cursor.close()
                    destino_cursor.close()
                    return JsonResponse({"message" : str(e) + str(sp_x)}, safe=False,status=500)
        
            origen_cursor.close()

            if len(errores) > 0:
               return JsonResponse(errores, safe=False,status=501) 

            return JsonResponse({"message" : "ok"}, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"message" : str(e)}, safe=False,status=500)


def reemplazarprocedure(texto):
    patron = r'\b(?:CREATE|ALTER)\s*\bPROCEDURE\b'
    reemplazo = 'CREATE OR ALTER PROCEDURE'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
def reemplazarfunction(texto):
    patron = r'\b(?:CREATE|ALTER)\s*\bFUNCTION\b'
    reemplazo = 'CREATE OR ALTER FUNCTION'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
def reemplazarview(texto):
    patron = r'\b(?:CREATE|ALTER)\s*\bVIEW\b'
    reemplazo = 'CREATE OR ALTER VIEW'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
