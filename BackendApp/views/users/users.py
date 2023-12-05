from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from BackendApp.models import *

from ...utils import *


@csrf_exempt
def users(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'GET':

        id = request_data["id"] if "id" in request_data else ''

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[spS_T_Usuarios] %s '''

        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(sp, (id,), database=database)
            print("The length of the response is " + str(len(response)))
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)


# THis method is for migrate users from WMS to USERS
    # if request.method == 'POST':

    #     id_employee = request.GET["id_employee"] if "id_employee" in request.GET else None
    #     warehouse = request.GET["warehouse"] if "warehouse" in request.GET else None

    #     response = []
    #     sp = ''' SET NOCOUNT ON
    #          EXEC [web].[sp_getUsuarios] %s, %s, %s'''

    #     # Query que se hace directamente a la base de datos
    #     try:
    #         response = exec_query(
    #             sp, (id_employee, database, warehouse,), database=database)

    #         response_dict = {}

    #         url = 'http://127.0.0.1:8001/api/register'

    #         for i in response:

    #             try:
    #                 i["activities_list"] = "1,2,2.1,2.5,3,3.1,3.2,3.3,3.4,3.5,3.6,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,6,6.1,6.2,7,7.1"
    #                 response_register = requests.post(
    #                     url, data=i)
    #                 print(response_register)
    #                 print(response_register.json())
    #                 response_dict[i['id_employee']] = str(response_register)
    #             except Exception as e:
    #                 print("Server Error!: ", e)
    #                 response_dict[i['id_employee']] = str(e)

    #         print("The length of the response is " + str(len(response)))

    #         return JsonResponse(response_dict, safe=False, status=200)
    #     except Exception as e:
    #         print("Server Error!: ", e)
    #         return JsonResponse('Server Error!', safe=False, status=500)

    elif request.method == 'POST':

        try:
            # id_employee = request.GET["id_employee"] if "id_employee" in request.GET else None
            warehouse = request_data["warehouse"] if "warehouse" in request_data else None
            user_name = request_data["user_name"] if "user_name" in request_data else None
            password = request_data["password"] if "password" in request_data else None
            email = request_data["email"] if "email" in request_data else None
            first_name = request_data["first_name"] if "first_name" in request_data else None
            last_name = request_data["last_name"] if "last_name" in request_data else None
            activities_list = request_data["activities_list"] if "activities_list" in request_data else None
            is_staff = request_data["is_staff"] if "is_staff" in request_data else None
            database_name = request_data["database_name"] if "database_name" in request_data else None
            role = request_data["role_"] if "role_" in request_data else 'user'
            id_customer = request_data["id_customer_"] if "id_customer_" in request_data else ''
            about = request_data["about"] if "about" in request_data else None

            response = []

            if user_name == None or password == None or email == None or first_name == None or last_name == None or activities_list == None or is_staff == None:
                return JsonResponse('Error al crear el usuario', safe=False, status=400)
            

            try:
                url_base = 'https://users.copernicowms.com/api/'
                # url_base = 'http://127.0.0.1:8000/api/'
                endpoint = 'validate/user'

                url = url_base + endpoint

                params = {
                    "user_name": user_name,
                    "email": email
                }

                validate_user = requests.get(url, params=params)

                if validate_user.status_code == 200:
                    print("El usuario ya existe")
                    return JsonResponse({"message" :"El usuario ya existe"}, safe=False, status=400)
            
            except Exception as e:
                print("Server Error!: ", e)
                return JsonResponse({"message" :"Error en la validación de usuario"}, safe=False, status=500)

            if database_name == None:
                database = request_data["database"]
                database_name = database
            else:
                database = database_name


            # if

            compania = warehouse
            if warehouse == None or warehouse == '':
                compania = TCompanias.objects.using(database).first() 
                compania = compania.codcia 
                warehouse = ''

            usuario = TUsuarios.objects.using(database).create(
                usuario=user_name,
                clave=password,
                grupo=1,
                # codcia=compania.codcia,
                codcia=compania,
                direlectronica=email,
                telefono='0000000000',
                cargo='Creado desde WMS',
                direccionip='44.209.250.151',
                nombrecompleto=first_name + ' ' + last_name,
                fechacreacion=datetime.now(),
                fechamodificacion=datetime.now(),
                fechainicio=datetime.now(),
                fechavencimiento=datetime.now() + timedelta(days=1000),
                estado=1,
                fechaultimaconexion=datetime.now(),
                adminmodificacion=0,
                idmac='8d42001529cbe2af')

            usuario.save(using=database)

            empleado = Templeados.objects.using(database).create(
                nombre=first_name,
                apellidos=last_name,
                fecha_nacimiento=datetime.now(),
                cedula='0000000000',
                telefono='0000000000',
                direccion='Creado desde WMS',
                cuentabancaria='0000000000',
                corporacion=compania,
                eps=1,
                numero_eps='-1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,-2',
                fechaingreso=datetime.now(),
                nivelempleado=usuario.id,
                area=6,
                estado=1)

            empleado.save(using=database)

            json = {
                "id_employee": empleado.id,
                "warehouse": warehouse,
                "user_name": usuario.usuario,
                "password": usuario.clave,
                "email": usuario.direlectronica,
                "first_name": empleado.nombre,
                "last_name": empleado.apellidos,
                "activities_list": activities_list,
                "database_name": database_name,
                "is_staff": is_staff,
                "is_active": 1,
                "is_superuser": 0,
                "role" : role,
                "id_customer" : id_customer, 
                "about" : about
            }

            print(json)

            endpoint = 'register'
            url = url_base + endpoint

            response_register = requests.post(url, json=json)

            if response_register.status_code == 200:
                print("Usuario creado correctamente")
                return JsonResponse({"message" :"Usuario creado correctamente"}, safe=False, status=200)

            else:
                print("Error al crear el usuario")
                print(response_register)
                print(response_register.json())
                return JsonResponse({"message" :"Error al crear el usuario"}, safe=False, status=500)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse({"message" :"Error en el servidor"}, safe=False, status=500)




    elif request.method == 'PUT':

        try:
            response = []

            if database != 'dll':
                return JsonResponse('Authorizarion failed', safe=False, status=500)

            database_name = request.GET["database_name"] if "database_name" in request.GET else None

            if database_name == None:
                return JsonResponse('Please provide a database name', safe=False, status=500)
            
            print(database_name)
            try:
                usuarios = TUsuarios.objects.using(database_name).all()
                print(usuarios)
                empleados = Templeados.objects.using(database_name).all()
                print(empleados)
            except Exception as e:
                print("Server Error!: ", e)
                return JsonResponse({"message" :str(e)}, safe=False, status=500)
            print('DATA OK')
            
            usuarios_creados = []
            usuarios_error = []
            
            for i in usuarios:
                for e in empleados:
                    if int(i.id) == int(e.nivelempleado):
                        try:
                            json = {
                                "id_employee": e.id,
                                "warehouse": i.codcia,
                                "user_name": i.usuario,
                                "password": i.clave,
                                "email": i.direlectronica,
                                "first_name": e.nombre,
                                "last_name": e.apellidos,
                                "activities_list": '1',
                                "database_name": database_name,
                                "is_staff": 0,
                                "is_active": 1,
                                "is_superuser": 0,
                                "role" : "user",
                                "id_customer" : None
                            }

                            url = 'https://users.copernicowms.com/api/register'
                            
                            response_register = requests.post(url, json=json)

                            if response_register.status_code == 200:
                                usuarios_creados.append(i.usuario)

                            else:
                                error_dict = { "usuario" : i.usuario, "error" : response_register.json() }
                                usuarios_error.append(error_dict)
                        except Exception as e:
                            error_dict = { "usuario" : i.usuario, "error" : str(e) }
                            usuarios_error.append(error_dict)

            response = {
                "usuarios_creados" : usuarios_creados,
                "usuarios_error" : usuarios_error
            }
            
            return JsonResponse(response, safe=False, status=200)
        
        except:
            return JsonResponse('Server Error!', safe=False, status=500)

        #     usuario.save(using=database)

        #     empleado = Templeados.objects.using(database).create(
        #         nombre=first_name,
        #         apellidos=last_name,
        #         fecha_nacimiento=datetime.now(),
        #         cedula='0000000000',
        #         telefono='0000000000',
        #         direccion='Creado desde WMS',
        #         cuentabancaria='0000000000',
        #         corporacion=compania,
        #         eps=1,
        #         numero_eps='-1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,-2',
        #         fechaingreso=datetime.now(),
        #         nivelempleado=usuario.id,
        #         area=6,
        #         estado=1)

        #     empleado.save(using=database)

        #     json = {
        #         "id_employee": empleado.id,
        #         "warehouse": warehouse,
        #         "user_name": usuario.usuario,
        #         "password": usuario.clave,
        #         "email": usuario.direlectronica,
        #         "first_name": empleado.nombre,
        #         "last_name": empleado.apellidos,
        #         "activities_list": activities_list,
        #         "database_name": database_name,
        #         "is_staff": is_staff,
        #         "is_active": 1,
        #         "is_superuser": 0
        #     }

        #     print(json)
        #     url = 'https://users.copernicowms.com/api/register'
        #     # url = 'http://127.0.0.1:8001/api/register'

        #     response_register = requests.post(url, json=json)

        #     if response_register.status_code == 200:
        #         print("Usuario creado correctamente")
        #         return JsonResponse('Usuario creado correctamente', safe=False, status=200)

        #     else:
        #         print("Error al crear el usuario")
        #         print(response_register)
        #         print(response_register.json())
        #         return JsonResponse('Error al crear el usuario', safe=False, status=500)

        # except Exception as e:
        #     print("Server Error!: ", e)
        #     return JsonResponse('Server Error!', safe=False, status=500)
