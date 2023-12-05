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
def massive_custommized(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':
        
        origin = request_data["origin"] if "origin" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else ""
        
        if origin is None:
            return JsonResponse({"message" : "origin is required"}, safe=False, status=405)
        elif destination is None:
            return JsonResponse({"message" : "destination is required"}, safe=False, status=405)
        
                
        try:
            errores = {}
            list_db = []
            #Adquirir lista de datos
            if destination == "":
                db_config = 'dll'
                c = config(db_config, '')
                collections = c.get_collections()   
                for collection in collections:
                    
                    if collection == origin:
                        continue
                    if collection == origin+"_adapter":
                        continue

                    if collection != 'activities':
                        if '_adapter' in origin:
                            list_db.append(collection + '_adapter')
                        else: 
                            list_db.append(collection)
            else: 
                for dest in destination:
                    if dest != 'activities':
                        if '_adapter' in origin:
                            list_db.append(dest + '_adapter')
                        else: 
                            list_db.append(dest)
            
            
            origen_cursor  = connections[origin].cursor()
            sp = 'dbo.dev_sp_customized_massive'
            sp_query = f"SELECT OBJECT_DEFINITION(OBJECT_ID('{sp}')) AS codigo_sp"
            origen_cursor.execute(sp_query)
            sp_codigo = origen_cursor.fetchone()[0]
            if sp_codigo is None:
                print(f"{sp} doesn't exist in origin database")
                return JsonResponse({"message" : f"{sp} doesn't exist in origin database"}, safe=False, status=405)
            sp_codigo = reemplazarprocedure(sp_codigo)
            
            for dest in list_db:
                print (f"-----> {dest}")
                try:
                    if '_adapter' in origin:
                        adapter_origin = settings.DATABASES[origin]['NAME']
                        base = origin.split('_')[0]
                        base_origin = settings.DATABASES[base]['NAME']     
                    else: 
                        base_origin = settings.DATABASES[origin]['NAME']
                        adapter_origin = settings.DATABASES[origin+"_adapter"]['NAME']
                    
                    if '_adapter' in dest:
                        adapter_destino = settings.DATABASES[dest]['NAME'] 
                        base = dest.split('_')[0]
                        base_destino = settings.DATABASES[base]['NAME']
                    else:
                        base_destino = settings.DATABASES[dest]['NAME']
                        adapter_destino = settings.DATABASES[dest+"_adapter"]['NAME']
                        
                    sp_codigo = sp_codigo.replace(str(base_origin),str(base_destino))
                    sp_codigo = sp_codigo.replace(str(adapter_origin),str(adapter_destino))
                    
                    destino_cursor  = connections[dest].cursor()
                    try:
                                                
                        destino_cursor.execute(sp_codigo)
                        
                        sp_customized = '''SET NOCOUNT ON
                                EXEC [dbo].[dev_sp_customized_massive]
                                ''' 
                        destino_cursor.execute(sp_customized)
                        
                        destino_cursor.close()
                        print(f"Ejecutado {sp} en {dest}")
                    except Exception as e:
                        destino_cursor.close()
                        print(e)
                        errores[dest] = str(e)
                except Exception as e:
                    errores[dest] = str(e)
                    print(e)
                    continue
            if len(errores) > 0:
                return JsonResponse(errores, safe=False,status=401) 
            return JsonResponse({"message" : "ok"}, safe=False, status=200)
        
        except Exception as e:
            print(e)
            return JsonResponse({"message" : str(e)}, safe=False,status=500)

def reemplazarprocedure(texto):
    patron = r'\b(?:CREATE|ALTER)\s*\bPROCEDURE\b'
    reemplazo = 'CREATE OR ALTER PROCEDURE'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
