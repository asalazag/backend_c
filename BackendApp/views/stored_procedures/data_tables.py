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
from datetime import datetime
@csrf_exempt
def insertdatatable(request):
    request_data = request._body
    if request.method == 'PUT':

        table = request_data["table"] if "table" in request_data else None
        origin = request_data["origin"] if "origin" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else ""
        if table is None:
            return JsonResponse({"message" : "table is required"}, safe=False, status=405)
        elif origin is None:
            return JsonResponse({"message" : "origin is required"}, safe=False, status=405)
        elif destination is None:
            return JsonResponse({"message" : "destination is required"}, safe=False, status=405)
        try:
            origen_cursor  = connections[origin].cursor()
            # for numero in range(115000, 117000):
            #     query = f"INSERT INTO T_PIC_multiproducto(cajap,productoEAN,referencia,entradas,salidas,loteproveedor,fechaultimomvto,idempleado) VALUES ({numero},'20049','811024463',100,0,'10',getdate(),1234)"
            #     print(query)
            #     destination_cursor  = connections[destination].cursor()
            #     destination_cursor.execute(query)
            # destination_cursor.close()
            # return JsonResponse({"message" : "ok"}, safe=False, status=200)
            errores = {}

            for table_x in table:
                try:
                    print(table_x + ' data ----> ' + destination)
                    sql_query = f'SELECT * FROM {table_x}'
                    origen_cursor.execute(sql_query)
                    columns = [column[0] for column in origen_cursor.description]
                    destination_cursor  = connections[destination].cursor()
                    destination_cursor.execute(sql_query)
                    exist = destination_cursor.fetchone()
                    if exist:
                        print('La tabla ya tiene datos')
                    else:
                        # Recorrer los resultados del cursor de origen
                        while True:
                            
                            # Obtener los datos de la fila actual del cursor de origen
                            row = origen_cursor.fetchone()
                            # Salir del bucle si no hay más filas
                            if row is None:
                                break
                            columns = [column[0] for column in origen_cursor.description]   
                            placeholders = [column for column in row]
                            if 'Id' in columns and isinstance(placeholders[0], int):
                                columns.remove('Id')
                                placeholders.remove(placeholders[0])
                            # print('El registro es:')
                            # print(placeholders)
                            placeholders_with_quotes = []
                            for value in placeholders:
                                if isinstance(value, str):
                                    placeholders_with_quotes.append(f"'{value}'")
                                elif value == None:
                                    placeholders_with_quotes.append('NULL')
                                elif value == False:
                                    placeholders_with_quotes.append(str(0))
                                elif value == True:
                                    placeholders_with_quotes.append(str(1))
                                elif isinstance(value, datetime):
                                    placeholders_with_quotes.append(str('getdate()'))
                                else:
                                    placeholders_with_quotes.append(str(value))                                 
                            
                            # print (placeholders_with_quotes)
                            query = f"INSERT INTO {table_x} ({', '.join(columns)}) VALUES ({', '.join(placeholders_with_quotes)})"
                            print(query)
                            destination_cursor.execute(query)
                
                except Exception as e:
                    print(e)
                    print(table_x)
                    origen_cursor.close()
                    destination_cursor.close()
                    return JsonResponse({"message" : str(e) + str(table_x)}, safe=False,status=500)
        
            origen_cursor.close()
            destination_cursor.close()

            if len(errores) > 0:
               return JsonResponse({"message" : str(e)}, safe=False,status=500)

            return JsonResponse({"message" : "ok"}, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"message" : str(e)}, safe=False,status=500)

