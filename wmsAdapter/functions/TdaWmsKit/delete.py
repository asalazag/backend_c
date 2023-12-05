from wmsAdapter.functions.TdaWmsKit.read import read_kit
import json
from django.utils import timezone
from wmsAdapter.models import TdaWmsKit
from django.http.response import JsonResponse



def delete_kit(productoean_pack, db_name):
    try:
        product = TdaWmsKit.objects.using(db_name).filter(productoean_pack=productoean_pack)
        if type(product) == str:
            return product
        else:
            if len(list(product)) == 0:
                return 'Product not found'
            for p in product:
                p.delete(using=db_name)
            return 'Deleted successfully'
    except Exception as e:
        print(e)
        return str(e.__cause__)