import json
from django.utils import timezone
from wmsAdapter.models import TdaWmsArt
from django.http.response import JsonResponse


def create_articles(request, db_name, request_data=None):

        if(request_data):
            pass
        elif(request.body):
            request_data = json.loads(request.body)
        else:
            return 'No data to create'

        fields = [field.name for field in TdaWmsArt._meta.get_fields()]

        # Check the fields 
        for r in request_data: 
            if r not in fields: 
                return "Field {} not found".format(r)

        final_fields = {}
        for f in fields:
            if f == "fecharegistro":
                final_fields[f] = timezone.now()

            elif f == "referencia":
                referencia = request_data.get(f,None)
                final_fields[f] = referencia
                if referencia == None:
                    return "Field {} is required".format(f)

            elif f == "nuevoean":
                nuevoean = request_data.get(f,None)
                final_fields[f] = nuevoean
                if nuevoean == None:
                    return "Field {} is required".format(f)

                else:
                    final_fields[f] = request_data.get(f,None)
            else:
                final_fields[f] = request_data.get(f, None)

        try:  
            product = TdaWmsArt.objects.using(db_name).filter(productoean=final_fields['productoean'])
            if len(list(product)) >= 1:
                return 'The product with productoean %s already exists' % final_fields['productoean']
            else:
                try:
                    TdaWmsArt.objects.using(db_name).create(**final_fields)

                    return 'created successfully'
                except Exception as e:
                    print(e)
                    return str(e.__cause__).lower()
        except Exception as e:
            print(e)
            return str(e.__cause__).lower()