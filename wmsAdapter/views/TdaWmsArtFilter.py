from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# #from inventory.functions.purchase_orders.read import *
from wmsAdapter.functions.TdaWmsArt.create import create_articles
from wmsAdapter.functions.TdaWmsArt.delete import delete_articles
from wmsAdapter.functions.TdaWmsArt.read import read_articles
from wmsAdapter.functions.TdaWmsArt.update import update_articles
from wmsAdapter.functions.TdaWmsArt.read_filter import readFilterArt
from wmsAdapter.models import *
from settings import *
from django.db.models import Q
from django.utils import timezone
# from django.shortcuts import render_to_response


@csrf_exempt
def filterart(request):

    try:
        db_name = request.db_name
        print(db_name)

    except Exception as e:
        return JsonResponse({'error': 'Apikey error'}, safe=False, status=500)

    # Get products
    if request.method == 'GET':

        try:
            response = readFilterArt(request, db_name=db_name)
            if type(response) == str:
                return JsonResponse({'message': response}, status=400)
            else:
                response_json = list(response.values())   # type: ignore
                return JsonResponse(response_json, safe=False, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Error getting article'}, safe=False, status=500)

