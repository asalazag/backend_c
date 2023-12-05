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
def create_alter_stored_procedures(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':

        function = request_data["function"] if "function" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else ""

        if function is None:
            return JsonResponse({"message" : "function is required"}, safe=False, status=405)
        
        try:
            if function == 'descripcion':
                grupo = request_data["grupo"] if "grupo" in request_data else None
                codigoDescripcion = request_data["codigoDescripcion"] if "codigoDescripcion" in request_data else None
                valordescripcion = request_data["valordescripcion"] if "valordescripcion" in request_data else None
                actualizaDescripcion = request_data["actualizaDescripcion"] if "actualizaDescripcion" in request_data else 0
                
                if grupo is None or codigoDescripcion is None or valordescripcion is None:
                    return JsonResponse({"message" : "grupo, codigoDescripcion, valordescripcion son required"}, safe=False, status=405)
                
                errores = {}
                if destination == "":
                    list_db=[]
                    db_config = 'dll'
                    c = config(db_config, '')
                    collections = c.get_collections()  
                    print (collections) 
                    for collection in collections:
                        if collection != 'activities':
                            list_db.append(collection)
                    print(list_db)       
                    for dest in list_db:
                        try:
                            sp = '''SET NOCOUNT ON
                                    EXEC dbo.dev_descripcionesexists %s,%s,%s,%s
                                    ''' 
                            try:
                                destino_cursor  = connections[dest].cursor()
                                destino_cursor.execute(sp,(grupo,codigoDescripcion,valordescripcion,actualizaDescripcion))
                                destino_cursor.close()
                            except Exception as e:
                                errores[dest] = str(e)
                        except Exception as e:
                            print(e)
                            destino_cursor.close()
                            return JsonResponse({"message" : str(e)}, safe=False,status=500)
                else:
                    sp = '''SET NOCOUNT ON
                                    EXEC dbo.dev_descripcionesexists %s,%s,%s,%s
                                    ''' 
                    destino_cursor  = connections[destination].cursor()
                    destino_cursor.execute(sp,(grupo,codigoDescripcion,valordescripcion,actualizaDescripcion))
                    destino_cursor.close()
                if len(errores) > 0:
                    return JsonResponse(errores, safe=False,status=501) 
                return JsonResponse({"message" : "ok"}, safe=False, status=200)
            
            if function == 'schema':
                errores = {}
                if destination == "":
                    list_db=[]
                    db_config = 'dll'
                    c = config(db_config, '')
                    collections = c.get_collections()   
                    for collection in collections:
                        if collection != 'activities':
                            list_db.append(collection)
                    print(list_db)       
                    for dest in list_db:
                        try:
                            query = 'CREATE SCHEMA bku'
                            try:
                                destino_cursor  = connections[dest].cursor()
                                destino_cursor.execute(query)
                                destino_cursor.close()
                            except Exception as e:
                                errores[dest] = str(e)
                        except Exception as e:
                            print(e)
                            destino_cursor.close()
                            return JsonResponse({"message" : str(e)}, safe=False,status=500)
                else:
                    query = 'CREATE SCHEMA bku'
                    destino_cursor  = connections[destination].cursor()
                    destino_cursor.execute(query)
                    destino_cursor.close()
                            
                return JsonResponse({"message" : "ok"}, safe=False, status=200)

            elif function == 'secuencia_picking':

                query = ''' CREATE SEQUENCE [dbo].[secuencia_picking] 
                            AS [int]
                                START WITH 3000
                                INCREMENT BY 1
                                MINVALUE 3000
                                MAXVALUE 2147483647
                                CACHE 
                            GO'''

                destino_cursor  = connections[destination].cursor()
                destino_cursor.execute(query)
                destino_cursor.close()
            
            elif function == 'secuencia_guias':
                query = ''' CREATE SEQUENCE [dbo].[secuencia_guias] 
                            AS [int]
                                START WITH 50000000
                                INCREMENT BY 1
                                MINVALUE 50000000
                                MAXVALUE 2147483647
                                CACHE 
                            '''

                destino_cursor  = connections[destination].cursor()
                destino_cursor.execute(query)
                destino_cursor.close()
            elif function == 'table':
                query = ''' CREATE TABLE [dbo].[tda_wms_epk_labels](
                            [id] [int] IDENTITY(1,1) NOT NULL,
                            [picking] [int] NULL,
                            [guia] [nvarchar](500) NULL,
                            [pdf] [nvarchar](max) NULL,
                            [fecharegistro] [datetime] NULL,
                        PRIMARY KEY CLUSTERED 
                        (
                            [id] ASC
                        )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
                        ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
                        '''
                destino_cursor  = connections[destination].cursor()
                destino_cursor.execute(query)
                destino_cursor.close()

                return JsonResponse({"message" : "ok"}, safe=False, status=200)
            else:
                return JsonResponse({"message" : "function is not valid"}, safe=False, status=405)
        
        except Exception as e:
            print(e)
            return JsonResponse({"message" : str(e)}, safe=False,status=500)


    if request.method == 'PUT':

        sp = request_data["sp"] if "sp" in request_data else None
        origin = request_data["origin"] if "origin" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else ""
        if sp is None:
            return JsonResponse({"message" : "sp is required"}, safe=False, status=405)
        elif origin is None:
            return JsonResponse({"message" : "origin is required"}, safe=False, status=405)
        elif destination is None:
            return JsonResponse({"message" : "destination is required"}, safe=False, status=405)
        try:
            origen_cursor  = connections[origin].cursor()
            
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
                list_db.append(str(destination)) 

            
            print(list_db)
            errores = {}

            for sp_x in sp:
                for dest in list_db:
                    try:
                        print(sp_x + ' ----> ' + dest)
                        sp_query = f"SELECT OBJECT_DEFINITION(OBJECT_ID('{sp_x}')) AS codigo_sp"
                        schemaquery = f"SELECT OBJECT_SCHEMA_NAME(OBJECT_ID('{sp_x}')) AS esquema_sp"
                        origen_cursor.execute(sp_query)
                        sp_codigo = origen_cursor.fetchone()[0]
                        origen_cursor.execute(schemaquery)
                        schemaObjet = origen_cursor.fetchone()[0]
                        if schemaObjet.lower() == 'dbo' or schemaObjet.lower() == 'web':
                            schemabku = "bku" + schemaObjet[0]
                        else:
                            schemabku = "bkum"
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
                        
                        if '_adapter' in dest:
                            adapter_destino = settings.DATABASES[dest]['NAME'] 
                            base = dest.split('_')[0]
                            base_destino = settings.DATABASES[base]['NAME']
                        else:
                            base_destino = settings.DATABASES[dest]['NAME']
                            adapter_destino = settings.DATABASES[dest+"_adapter"]['NAME']
                        
                        # print('BASES OK')

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
                                destino_cursor  = connections[dest].cursor()
                                destino_cursor.execute(f"SELECT 1 FROM sys.schemas WHERE name = '{schemaObjet}'")
                                existschema = destino_cursor.fetchone()
                                if not existschema:
                                    destino_cursor.execute(f"CREATE SCHEMA {schemaObjet}")
                                    print(f"Schema {schemaObjet} created in {dest}.")
                                try:
                                    destino_cursor.execute(sp_query)
                                    sp_codigoact = destino_cursor.fetchone()[0]
                                    destino_cursor.close()
                              
                                    sp_codigoactver = reemplazarfunction(sp_codigoact)
                                    sp_codigoactver = reemplazarprocedure(sp_codigoactver)
                                    sp_codigoactver = reemplazarview(sp_codigoactver)

                                except Exception as e:
                                    pass
                            except Exception as e:
                                print(e)
                                destino_cursor.close()
                                errores[dest] = str(e)
                            if sp_codigoactver == sp_codigo:
                                print(f"{sp_x} is the same in {dest} database")
                                # # sp_codigo = sp_codigo.replace('CREATE','CREATE OR ALTER')
                                # # sp_codigo = sp_codigo.replace('create','CREATE OR ALTER')
                                # destino_cursor  = connections[dest].cursor()
                                # destino_cursor.execute(sp_codigo)
                                # destino_cursor.close()
                                continue
                            else:
                                destino_cursor  = connections[dest].cursor()
                                if sp_codigoact != "" and sp_codigoact is not None :
                                    print(f"{sp_x} exist in {dest} database --- > Create [{schemabku}]")
                                    try:
                                        destino_cursor.execute(f"SELECT 1 FROM sys.schemas WHERE name = '{schemabku}'")
                                        exists = destino_cursor.fetchone()
                                        if not exists:
                                            # Crear el esquema
                                            # querycrt = '''
                                            #     CREATE SCHEMA %s
                                            #     '''
                                            # destino_cursor.execute(querycrt,schemabku)
                                            destino_cursor.execute(f"CREATE SCHEMA {schemabku}")
                                            print(f"Schema '{schemabku}' created in {dest}.")
                                        sp_codigoact = reemplazarprocedurebackup(sp_codigoact, schemabku,schemaObjet)
                                        sp_codigoact = reemplazarfunctionbackup(sp_codigoact, schemabku,schemaObjet)
                                        sp_codigoact = reemplazarviewbackup(sp_codigoact, schemabku,schemaObjet)
                                        # print(sp_codigoact)
                                        destino_cursor.execute(sp_codigoact)
                                        print(f"Backup created in {dest}.")
                                    except Exception as e:
                                        pass
                                                                                            
                                destino_cursor.execute(sp_codigo)
                                destino_cursor.close()
                                print(f"Objet created  in {dest}")
                        except Exception as e:
                            errores[dest] = str(e)
                      
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
def reemplazarviewbackup(texto, schemabku, schemaObjet):
    #patron = r'CREATE\s+VIEW\s+\[(dbo|web)\]'
    patron = r'CREATE\s+VIEW\s+\[(dbo|web|' + re.escape(schemaObjet) + r')\]'
    reemplazo = f'CREATE OR ALTER VIEW [{schemabku}]'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
def reemplazarprocedurebackup(texto, schemabku, schemaObjet):
    #patron = r'CREATE\s+PROCEDURE\s+\[(dbo|web)\]'
    patron = r'CREATE\s+PROCEDURE\s+\[(dbo|web|' + re.escape(schemaObjet) + r')\]'
    print(patron)
    reemplazo = f'CREATE OR ALTER PROCEDURE [{schemabku}]'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
def reemplazarfunctionbackup(texto, schemabku, schemaObjet):
    #patron = r'CREATE\s+FUNCTION\s+\[(dbo|web)\]'
    patron = r'CREATE\s+FUNCTION\s+\[(dbo|web|' + re.escape(schemaObjet) + r')\]'
    reemplazo = f'CREATE OR ALTER FUNCTION [{schemabku}]'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado