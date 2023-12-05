import json
from wmsAdapter.functions.TdaWmsKit.read import read_kit
from django.utils import timezone
from wmsAdapter.models import TdaWmsKit

def update_kit(request, db_name, request_data=None):
    if(request_data):
        pass
    elif(request.body):
        request_data = dict(request.body)
    else:
        return 'No data to update'
    
    if 'database' in request_data:
            request_data.pop('database')
            request_data.pop('id_employee')
            request_data.pop('warehouse')
            request_data.pop('id_customer')
            request_data.pop('role')
    
    if len(request_data) == 0:
        return 'No data to update'

    fields = [field.name for field in TdaWmsKit._meta.get_fields()]
    
    # Check the fields 
    for r in request_data: 
        if r not in fields: 
            return "Field {} not found in the body".format(r)

    final_fields = {}
    for f in fields:
        if f == "fecharegistro":
            final_fields[f] = timezone.now()
        elif f == "id":
            id = request_data.get(f,None)
            if id == None:
                return "Field {} is required".format(f)
            # print(id)
        else:
            final_fields[f] = request_data.get(f, None)

    try:   
        product = TdaWmsKit.objects.using(db_name).filter(id=id)
        if type(product) == str:
            return product
        else:
            if len(list(product)) == 1:
                product = product[0]
                for key, value in final_fields.items():
                    setattr(product, key, value)
                product.save(using=db_name)
            
                return "Updated successfully"

            elif len(list(product)) == 0:
                return "No product found"
            else:
                return "Only one product can be updated at a time"
    except Exception as e:
        print(e)
        return str(e.__cause__)