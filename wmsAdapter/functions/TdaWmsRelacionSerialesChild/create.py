import json
from django.utils import timezone
from wmsAdapter.models import TdaWmsRelacionSerialesChild
from django.http.response import JsonResponse


def create_seriales(request, db_name, request_data=None):
    if(request_data):
        pass
    elif(request.body):
        request_data = json.loads(request.body)
    else:
        return 'No data to create'

    fields = [field.name for field in TdaWmsRelacionSerialesChild._meta.get_fields()]

    # Check the fields
    for r in request_data:
        if r not in fields:
            return "Field {} not found".format(r)

    final_fields = {}
    for f in fields:
        if f == 'id':
            pass
        else:
            final_fields[f] = request_data.get(f, None)


    try:
        try:
            TdaWmsRelacionSerialesChild.objects.using(db_name).create(**final_fields)

            return 'created successfully'
        except Exception as e:
            print(e)
            return str(e.__cause__).lower()
    except Exception as e:
        print(e)
        return str(e.__cause__).lower()
