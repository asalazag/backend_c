from django.db.models import Q

from wmsAdapter.models import VTPicMultiproducto

def read_vtpicmp(request, db_name):

        params = dict(request.GET)

        fields = [field.name for field in VTPicMultiproducto._meta.get_fields()]

        # Check the fields 
        for p in params: 
            if p not in fields: 
                return "Field {} not found".format(p)

        final_fields = {}
        for f in fields:
            final_fields[f] = request.GET.get(f,'')

        # print(final_fields)

        query = Q()
        for key, value in final_fields.items():
            if value != '':
                query &= Q(**{key: value})
        
        
        try:    

            response = VTPicMultiproducto.objects.using(db_name).filter(query)[:500]
            return response

        except Exception as e:
            print(e)
            return None