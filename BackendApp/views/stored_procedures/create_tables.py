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

def create_alter_tables(request):
    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':
        table = request_data["table"] if "table" in request_data else None
        origin = request_data["origin"] if "origin" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else ""
     
        # Obtener la definición de la tabla desde la base de datos de origen
        origen_cursor  = connections[origin].cursor()
        # origen_cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'")
        # columnas = origen_cursor.fetchall()

        destino_cursor  = connections[destination].cursor()
        validacion = f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table}'"
        
        origen_cursor.execute(validacion)
        existe_origen = origen_cursor.fetchone()[0]
        if existe_origen == 0:
            print("La tabla no existe en la base de datos de origen")
            return JsonResponse({"error": "La tabla no existe en la base de datos de origen"}, status=400)
        destino_cursor.execute(validacion)
        existe_destino = destino_cursor.fetchone()[0]
        if existe_destino == 1:
            print("La tabla ya existe en la base de datos de destino")
            return JsonResponse({"error": "La tabla ya existe en la base de datos de destino"}, status=400)

        # Consulta para obtener la información de las columnas
        sql = f"SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, NUMERIC_SCALE,COLUMN_DEFAULT, IS_NULLABLE \
                FROM INFORMATION_SCHEMA.COLUMNS \
                WHERE TABLE_NAME = '{table}'"

        # Ejecutar la consulta
        origen_cursor.execute(sql)


        # Obtener los resultados
        columns = origen_cursor.fetchall()
        # print(resultados)

        # Crear el comando CREATE TABLE
        create_table = f"CREATE TABLE {table} (\n"
        
        # Recorrer cada columna y agregarla al comando CREATE TABLE
        for column in columns:
            column_name = column[0]
            data_type = column[1]
            max_length = column[2]
            numeric_precision = column[3]
            numeric_scale = column[4]
            default_value = column[5] if column else None
            is_nullable = column[6] if column else None

            # Determinar el tipo y los valores según el tipo de dato
            if data_type == 'decimal':
                column_type = f"DECIMAL({numeric_precision}, {numeric_scale})"
            elif data_type == 'nvarchar':
                column_type = f"NVARCHAR({max_length if str(max_length) != '-1' else 'max'})"
            elif data_type == 'varchar':
                column_type = f"VARCHAR({max_length})"
            elif data_type == 'char':
                column_type = f"CHAR"
            elif data_type == 'float':
                column_type = "FLOAT"
            elif data_type == 'int':
                column_type = "INT"
            elif data_type == 'datetime':
                column_type = "DATETIME"
            elif data_type == 'date':
                column_type = "DATE"
            else:
                column_type = data_type

            # Agregar la columna al comando CREATE TABLE con la información de valor por defecto y NULL o NOT NULL
            create_table += f"    {column_name} {column_type} "

            if default_value is not None:
                create_table += f" DEFAULT {default_value}"

            if is_nullable == 'NO':
                create_table += " NOT NULL"
            create_table += ",\n"
            
            # # Consultar si la columna es una clave foránea
            # query_fk = f"SELECT COLUMN_NAME, CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = '{table}' AND COLUMN_NAME = '{column_name}'"
            # origen_cursor.execute(query_fk)
            # result_fk = origen_cursor.fetchone()

            # if result_fk:
            #     # La columna es una clave foránea
            #     fk_column_name = result_fk[0]
            #     fk_constraint_name = result_fk[1]
            #     fk_referenced_table = result_fk[3]

            #     create_table += f"    FOREIGN KEY ({fk_column_name}) REFERENCES {fk_referenced_table} (columna_referenciada),\n"  # Reemplaza "columna_referenciada" con el nombre real de la columna referenciada

        # Obtener la información de la llave primaria
        query_pk = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = '{table}' AND CONSTRAINT_NAME LIKE 'PK_%'"
        origen_cursor.execute(query_pk)
        primary_keys = origen_cursor.fetchall()

        if primary_keys:
            # Agregar la definición de la llave primaria al comando CREATE TABLE
            primary_key_columns = [pk[0] for pk in primary_keys]
            primary_key_columns_str = ", ".join(primary_key_columns)
            create_table += f"    PRIMARY KEY ({primary_key_columns_str}),\n"
        
        # Eliminar la última coma y agregar el cierre del comando CREATE TABLE
        create_table = create_table.rstrip(",\n") + "\n)"

        print(create_table)
        destino_cursor.execute(create_table)
        # Mostrar el comando CREATE TABLE
        

        # Cerrar el cursor y la conexión
        origen_cursor.close()
        destino_cursor.close()

        return JsonResponse({'message': 'OK'}, status=200)


    # this method is for alter table
    if request.method == 'PUT':
        table = request_data["table"] if "table" in request_data else None
        origin = request_data["origin"] if "origin" in request_data else None
        destination = request_data["destination"] if "destination" in request_data else ""

        print(f"table: {table} ")

        try:
            # Obtener la definición de la tabla desde la base de datos de origen
            origen_cursor  = connections[origin].cursor()
            # origen_cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'")
            # columnas = origen_cursor.fetchall()
            
            destino_cursor  = connections[destination].cursor()

            validacion = f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table}'"
        
            origen_cursor.execute(validacion)
            existe_origen = origen_cursor.fetchone()[0]
            if existe_origen == 0:
                print("La tabla no existe en la base de datos de origen")
                return JsonResponse({"error": "La tabla no existe en la base de datos de origen"}, status=400)
            destino_cursor.execute(validacion)
            existe_destino = destino_cursor.fetchone()[0]
            if existe_destino == 0:
                print("La tabla no existe en la base de datos de destino")
                return JsonResponse({"error": "La tabla no existe en la base de datos de destino"}, status=400)
            # Consulta para obtener la información de las columnas
            sql = f"SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, NUMERIC_SCALE,COLUMN_DEFAULT, IS_NULLABLE \
                    FROM INFORMATION_SCHEMA.COLUMNS \
                    WHERE TABLE_NAME = '{table}'"
            
            # Ejecutar la consulta
            origen_cursor.execute(sql)
            # Obtener los resultados
            columnsOrigen = origen_cursor.fetchall()
            # Ejecutar la consulta
            destino_cursor.execute(sql)
            # Obtener los resultados
            columnsDestino = destino_cursor.fetchall()
            # print('origen-----------------')
            # print(columnsOrigen)
            # print('destino-----------------')
            # print(columnsDestino)
            columnas = []
            #comparar columnas en los arreglos y guardar solo als diferentes
            if len(columnsOrigen) == 0 and len(columnsDestino) == 0:
                print('the tables are empty')
            else:
                for column in columnsOrigen:
                    column_name = column[0]  # Get the column name
                    if column not in columnsDestino and column_name.lower() not in [col[0].lower() for col in columnsDestino]:
                        columnas.append(column)
                if len(columnas) == 0:
                    print('the tables are equal')
                else:
                    alter_table = f"ALTER TABLE {table} \n"
                    print(f"ALTER TABLE ----> {table}")
                    # print(columnas)
                    alter_table += "ADD "
                    for column in columnas:
                        column_name = column[0]
                        data_type = column[1]
                        max_length = column[2]
                        numeric_precision = column[3]
                        numeric_scale = column[4]
                        default_value = column[5] if column else None
                        is_nullable = column[6] if column else False
                        # Determinar el tipo y los valores según el tipo de dato
                        if data_type == 'decimal':
                            column_type = f"DECIMAL({numeric_precision}, {numeric_scale})"
                        elif data_type == 'nvarchar':
                            column_type = f"NVARCHAR({max_length if str(max_length) != '-1' else 'max'})"
                        elif data_type == 'varchar':
                            column_type = f"VARCHAR({max_length})"
                        elif data_type == 'char':
                            column_type = f"CHAR"
                        elif data_type == 'float':
                            column_type = "FLOAT"
                        elif data_type == 'int':
                            column_type = "INT"
                        elif data_type == 'datetime':
                            column_type = "DATETIME"
                        elif data_type == 'date':
                            column_type = "DATE"
                        else:
                            column_type = data_type
                        
                        # Agregar la columna al comando CREATE TABLE con la información de valor por defecto y NULL o NOT NULL
                        alter_table += f"[{column_name}] {column_type}"
                        if is_nullable:
                            alter_table += " NULL"
                        else:
                            alter_table += " NOT NULL"
                        if default_value is not None:
                            alter_table += f" DEFAULT {default_value}"
                        alter_table += ",\n"   
                    alter_table = alter_table.rstrip(",\n") + ";\n"
                    print(alter_table)
                    # return JsonResponse({'message': alter_table}, status=200)
                    destino_cursor.execute(alter_table)
                    print('finish modify table {table} in {destination} database')
            origen_cursor.close()
            destino_cursor.close()            

            return JsonResponse({'message': 'OK'}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({'message': str(e)}, status=500)
    else:

        return JsonResponse({'message': 'Invalid request method'}, status=405)


        # print(columnas)
        
        # sql_creacion = f"CREATE TABLE {table} ("
        # for columna in columnas:
        #     nombre_columna = columna[0]
        #     tipo_dato = columna[1]
        #     values = columna[2]
        #     sql_creacion += f"{nombre_columna} {tipo_dato} {tipo_dato}, "
        # print(sql_creacion)

        # return JsonResponse({"message" : "OK"}, safe=False, status=200)
        # try:
        #     cursor = connections[database].cursor()
        #     cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG = '"+database+"'")
        #     tables = cursor.fetchall()
        #     for table in tables:
        #         table_name = table[0]
        #         cursor.execute("SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"+table_name+"' AND TABLE_CATALOG = '"+database+"'")
        #         columns = cursor.fetchall()
        #         print(table_name)
        #         print(columns)
        #         cursor.execute("SELECT CONSTRAINT_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = '"+table_name+"' AND TABLE_CATALOG = '"+database+"'")
        #         constraints = cursor.fetchall()
        #         print(constraints)
        #         print("----------------------------------------------------")
        #     return JsonResponse({"message" : "ok"}, safe=False, status=200)
        # except Exception as e:
        #     return JsonResponse({"message" : str(e)}, safe=False,status=500)


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
def reemplazarviewbackup(texto):
    patron = r'CREATE\s+VIEW\s+\[(dbo|web)\]'
    reemplazo = 'CREATE OR ALTER VIEW [bku]'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
def reemplazarprocedurebackup(texto):
    patron = r'CREATE\s+PROCEDURE\s+\[(dbo|web)\]'
    reemplazo = 'CREATE  OR ALTER PROCEDURE [bku]'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado
def reemplazarfunctionbackup(texto):
    patron = r'CREATE\s+FUNCTION\s+\[(dbo|web)\]'
    reemplazo = 'CREATE OR ALTER FUNCTION [bku]'
    resultado = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return resultado

