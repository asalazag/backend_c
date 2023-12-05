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
def equalize_update_procedures(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':

        origin = request_data["origin"] if "origin" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else None
        if origin is None:
            return JsonResponse({"message" : "origin is required"}, safe=False, status=405)
        elif destination is None:
            return JsonResponse({"message" : "destination is required"}, safe=False, status=405)
        try:
            list_sp_base = []
            list_sp_origin = []
            list_sp_destination = []

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
            destination_cursor  = connections[destination].cursor()
            querysearch = "EXEC [dbo].[dev_find_] ''"

            origen_cursor.execute(querysearch)
            response = origen_cursor.fetchall()
            list_sp_origin = [row[0] for row in response]
            #imprimir longitud de arreglo
            print(len(list_sp_origin))
            # print(list_sp_origin)
            destination_cursor.execute(querysearch)
            response = destination_cursor.fetchall()
            list_sp_destination = [row[0] for row in response]
            print(len(list_sp_destination))
            # print(list_sp_destination)

            for sp in list_sp_origin:
                if sp not in list_sp_destination:
                    list_sp_base.append(sp)
            print(len(list_sp_base))
            
            # for sp_x in list_sp_base:
            #     print(sp_x + ' ----> ' + destination)
            #     sp_query = f"SELECT OBJECT_DEFINITION(OBJECT_ID('{sp_x}')) AS codigo_sp"
            #     origen_cursor.execute(sp_query)
            #     sp_codigo = origen_cursor.fetchone()[0]
            #     sp_codigo = sp_codigo.replace(str(base_origin),str(base_destino))
            #     sp_codigo = sp_codigo.replace(str(adapter_origin),str(adapter_destino))
                # print(sp_codigo)
            if len(list_sp_base) == 0:
                return JsonResponse({"message" : "No hay objetos para actualizar"}, safe=False, status=405)
            errores = {}
            
            for sp_x in list_sp_base:
                try:
                    print(sp_x + ' ----> ' + destination)
                    sp_query = f"SELECT OBJECT_DEFINITION(OBJECT_ID('{sp_x}')) AS codigo_sp"
                    schemaquery = f"SELECT OBJECT_SCHEMA_NAME(OBJECT_ID('{sp_x}')) AS esquema_sp"
                    origen_cursor.execute(sp_query)
                    sp_codigo = origen_cursor.fetchone()[0]
                    origen_cursor.execute(schemaquery)
                    schemaObjet = origen_cursor.fetchone()[0]
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
                        sp_codigo = reemplazarfunction(sp_codigo)
                        sp_codigo = reemplazarprocedure(sp_codigo)
                        sp_codigo = reemplazarview(sp_codigo)
                        try:
                            destino_cursor  = connections[destination].cursor()
                            destino_cursor.execute(f"SELECT 1 FROM sys.schemas WHERE name = '{schemaObjet}'")
                            existschema = destino_cursor.fetchone()
                            if not existschema:
                                destino_cursor.execute(f"CREATE SCHEMA {schemaObjet}")
                                print(f"Schema {schemaObjet} created in {destination}.")
                        except Exception as e:
                            destino_cursor.close()
                            errores[sp_x] = str(e)
                        destino_cursor  = connections[destination].cursor()                                                        
                        destino_cursor.execute(sp_codigo)
                        destino_cursor.close()
                        print(f"Objet created  in {destination}")     
                    except Exception as e:
                        print(e)
                        errores[sp_x] = str(e)
                        continue
                    
                except Exception as e:
                    print(e)
                    origen_cursor.close()
                    destino_cursor.close()
                    continue    
        
            origen_cursor.close()

            if len(errores) > 0:
               return JsonResponse(errores, safe=False,status=501) 

            return JsonResponse({"message" : "ok"}, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"message" : str(e)}, safe=False,status=500)


def reemplazarprocedure(texto):
    patron = r'\b(?:CREATE)\s*\bPROCEDURE\b'
    reemplazo = 'CREATE PROCEDURE'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
def reemplazarfunction(texto):
    patron = r'\b(?:CREATE)\s*\bFUNCTION\b'
    reemplazo = 'CREATE FUNCTION'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
def reemplazarview(texto):
    patron = r'\b(?:CREATE)\s*\bVIEW\b'
    reemplazo = 'CREATE VIEW'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
