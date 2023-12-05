import json
from django.utils import timezone
from wmsAdapter.models import TdaWmsKit
from django.http.response import JsonResponse


def create_kit(request, db_name, request_data=None):
        
        if(request_data):
            pass
        elif(request.body):
            request_data = dict(request.body)
        else:
            return 'No data to create'

        if 'database' in request_data:
            request_data.pop('database')
            request_data.pop('id_employee')
            request_data.pop('warehouse')
            request_data.pop('id_customer')
            request_data.pop('role')
        

        fields = [field.name for field in TdaWmsKit._meta.get_fields()]
        
        print(request_data)   

        for r in request_data: 
            if r not in fields: 
                return "Field {} not found".format(r)
            
        final_fields = {}
        for f in fields:
            if f == "fecharegistro":
                final_fields[f] = timezone.now()
        
            elif f == "productoean_pack":
                productoean_pack = request_data.get(f,None)
                final_fields[f] = productoean_pack
                if productoean_pack == None:
                    return "Field {} is required".format(f)
                
            elif f == "productoean_product":
                productoean_product = request_data.get(f,None)
                final_fields[f] = productoean_product
                if productoean_product == None:
                    return "Field {} is required".format(f)

            elif f == "bodega":
                bodega = request_data.get(f,None)
                final_fields[f] = bodega
                if bodega == None:
                    return "Field {} is required".format(f)
                else:
                    final_fields[f] = request_data.get(f,None)
            else:
                final_fields[f] = request_data.get(f, None)
        try:  
            product = TdaWmsKit.objects.using(db_name).filter(productoean_pack=final_fields['productoean_pack'], productoean_product=final_fields['productoean_product'])
            if len(list(product)) >= 1:
                return 'The Kit already exist'
            else:
                try:
                    TdaWmsKit.objects.using(db_name).create(**final_fields)
                    return 'created successfully'
                except Exception as e:
                    print(e)
                    return str(e.__cause__).lower()
        except Exception as e:
            print(e)
            return str(e.__cause__).lower()