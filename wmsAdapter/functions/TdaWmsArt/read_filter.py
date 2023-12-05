from django.db.models import Q
from wmsAdapter.models import TdaWmsArt
from datetime import datetime, timedelta

def readFilterArt(request, db_name):

        params = dict(request.GET)


        if 'fecha_inicial' in params:
            fecha_inicial = params['fecha_inicial'][0] 
            params.pop('fecha_inicial')
        else:
            fecha_inicial = '2000-01-01'

        if 'fecha_final' in params:
            current_date = datetime.strptime(params['fecha_final'][0], '%Y-%m-%d')
            current_date = current_date + timedelta(days=1)
            fecha_final = current_date.strftime('%Y-%m-%d')
            params.pop('fecha_final')
        else:
            current_date = datetime.today().strftime('%Y-%m-%d')
            current_date = datetime.strptime(current_date, '%Y-%m-%d')
            current_date = current_date + timedelta(days=1)
            fecha_final = current_date.strftime('%Y-%m-%d')
            

        fields = [field.name for field in TdaWmsArt._meta.get_fields()]

        # Check the fields 
        for p in params: 
            if p not in fields: 
                return "Field {} not found".format(p)

        final_fields = {}
        for f in fields:
            if f != "tdawmsduk" and f != "tdawmsdpk":  #Foreign keys
                final_fields[f] = request.GET.get(f,'')

        # print(fields)
        # print(final_fields)

        query = Q()
        for key, value in final_fields.items():
            if value != '':
                query &= Q(**{f'{key}__icontains': value})
        
        # print(query)
        
        try:    

            response = TdaWmsArt.objects.using(db_name).filter(query,Q(fecharegistro__range=[fecha_inicial, fecha_final]) | Q(fecharegistro__isnull=True)).order_by('-fecharegistro')[:10]
            return response

        except Exception as e:
            print(e)
            return None