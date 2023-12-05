import json
from wmsAdapter.functions.TdaWmsEpn.read import read_epn

from wmsAdapter.models import TdaWmsEpn

def update_epn(request, db_name):

    if(request.body):
        request_data = json.loads(request.body)
    else:
        return 'No data to update'

    if len(request_data) == 0:
        return 'No data to update'

    fields = [field.name for field in TdaWmsEpn._meta.get_fields()]


    # Check the fields 
    for r in request_data: 
        if r not in fields: 
            return "Field {} not found in the body".format(r)

    final_fields = {}
    for f in fields:
        if f == "tipodocto":
            if request_data.get(f,None) != None:
                return "The tipodocto field cannot be updated"
        if f == "doctoerp":
            if request_data.get(f,None) != None:
                return "The doctoerp field cannot be updated"
        if f == "item":
            if request_data.get(f,None) != None:
                return "The item field cannot be updated"
        if f == "bodega":
            if request_data.get(f,None) != None:
                return "The bodega field cannot be updated"
        if f == "productoean":
            if request_data.get(f,None) != None:
                return "The productoean field cannot be updated"
                
        final_fields[f] = request_data.get(f,None)
        if final_fields[f] == None:
            final_fields.pop(f) 
    
    try:    
        epn = read_epn(request, db_name=db_name)
        if type(epn) == str:
            return epn
        else:
            if len(list(epn)) == 1:
                epn = epn[0]
                for key, value in final_fields.items():
                    setattr(epn, key, value)
                epn.save(using=db_name)
            
                return "Updated successfully"

            elif len(list(epn)) == 0:
                return "No register found"
            else:
                return "Only one product can be updated at a time"
    except Exception as e:
        print(e)
        return str(e.__cause__)