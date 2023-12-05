import json
from django.utils import timezone
from wmsAdapter.models import TdaWmsClt
from django.http.response import JsonResponse


def create_clt(request, db_name, request_data=None):


        print('aqui')

        if(request_data):
            pass
        elif(request.body):
            request_data = dict(request.body)
            # request_data = json.loads(request.body)
        else:
            return 'No data to create'
        
        print(request_data)
        if 'database' in request_data:
            del request_data['database']

        if 'id_employee' in request_data:
            del request_data['id_employee']
        
        if 'warehouse' in request_data:
            del request_data['warehouse']

        if 'id_customer' in request_data:
            del request_data['id_customer']

        if 'role' in request_data:
            del request_data['role']

        fields = [field.name for field in TdaWmsClt._meta.get_fields()]

        # Check the fields 
        for r in request_data: 
            if r not in fields: 
                return "Field {} not found".format(r)


        final_fields = {}
        for f in fields:
            if f == "fechaplaneacion":
                final_fields[f] = timezone.now()
            elif f == "fechapedido":
                final_fields[f] = timezone.now()
            else:
                final_fields[f] = request_data.get(f,None)

        try:    
            try:
                TdaWmsClt.objects.using(db_name).create(**final_fields)

                return 'created successfully'
            except Exception as e:
                print(e)
                return str(e.__cause__).lower()
        except Exception as e:
            print(e)
            return str(e.__cause__).lower()