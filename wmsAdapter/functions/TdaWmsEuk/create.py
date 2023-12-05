import json
from django.utils import timezone
from wmsAdapter.models import TdaWmsEuk
from django.http.response import JsonResponse


def create_euk(request, db_name, request_data=None):

    if (request_data):
        pass
    elif (request.body):
        print(request.body)
        try:
            request_data = json.loads(request.body)
        except:
            request_data = request.body
    else:
        return 'No data to create'

    if 'database' in request_data:
        request_data.pop('database')
        request_data.pop('id_employee')
        request_data.pop('warehouse')

    fields = [field.name for field in TdaWmsEuk._meta.get_fields()]

    # Check the fields
    for r in request_data:
        if r not in fields:
            return "Field {} not found".format(r)

    final_fields = {}
    for f in fields:
        if f != "tdawmsduk":

            # Date fields
            if f == "fecharegistro":
                final_fields[f] = timezone.now()
            elif f == "fecha":
                final_fields[f] = timezone.now()
            elif f == "f_ultima_actualizacion":
                final_fields[f] = timezone.now()

            # required fields
            elif f == "numdocumento":
                numdocumento = request_data.get(f, None)
                final_fields[f] = numdocumento
                if numdocumento == None:
                    return "Field {} is required".format(f)

            elif f == "tipodocto":
                tipodocto = request_data.get(f, None)
                final_fields[f] = tipodocto
                if tipodocto == None:
                    return "Field {} is required".format(f)

            elif f == "doctoerp":
                doctoerp = request_data.get(f, None)
                final_fields[f] = doctoerp
                if doctoerp == None:
                    return "Field {} is required".format(f)

            elif f == "item":
                item = request_data.get(f, None)
                final_fields[f] = item
                if item == None:
                    return "Field {} is required".format(f)

            else:
                final_fields[f] = request_data.get(f, None)

    try:
        try:
            TdaWmsEuk.objects.using(db_name).create(**final_fields)

            return 'created successfully'
        except Exception as e:
            print(e)
            return str(e.__cause__).lower()
    except Exception as e:
        print(e)
        return str(e.__cause__).lower()
