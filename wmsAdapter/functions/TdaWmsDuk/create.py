import json
from django.utils import timezone
from wmsAdapter.models import TdaWmsDuk
from django.http.response import JsonResponse


def create_duk(request, db_name, request_data=None):

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

    fields = [field.name for field in TdaWmsDuk._meta.get_fields()]

    # Check the fields
    for r in request_data:
        if r not in fields:
            return "Field {} not found".format(r)

    final_fields = {}
    for f in fields:
        if f == "fecharegistro":
            final_fields[f] = timezone.now()   
        else:
            final_fields[f] = request_data.get(f, None)

    try:
        try:
            TdaWmsDuk.objects.using(db_name).create(**final_fields)

            return 'created successfully'
        except Exception as e:
            print(e)
            return str(e.__cause__).lower()
    except Exception as e:
        print(e)
        return str(e.__cause__).lower()
