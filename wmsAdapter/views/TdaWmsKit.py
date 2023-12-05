from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# #from inventory.functions.purchase_orders.read import *
from wmsAdapter.functions.TdaWmsKit.create import create_kit
from wmsAdapter.functions.TdaWmsKit.delete import delete_kit
from wmsAdapter.functions.TdaWmsKit.read import read_kit
from wmsAdapter.functions.TdaWmsKit.update import update_kit
from wmsAdapter.models import *
from settings import *
from django.db.models import Q
from django.utils import timezone
import copy
# from django.shortcuts import render_to_response


@csrf_exempt
def kit(request):

    try:
        db_name = request.db_name
        print(db_name)

    except Exception as e:
        return JsonResponse({'error': 'Apikey error'}, safe=False, status=500)

    # Get products
    if request.method == 'GET':

        try:
            response = read_kit(request, db_name=db_name)
            if type(response) == str:
                return JsonResponse({'message': response}, status=400)
            else:
                response_json = list(response.values())   # type: ignore
                return JsonResponse(response_json, safe=False, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Error getting Kit'}, safe=False, status=404)

  # Create a new Kit
    if request.method == 'POST':
        try:
            request_data = dict(request.body)          
            productos=request_data.get('productos',None)
            
            if productos == None:
                return JsonResponse({'message': 'Field productos is required'}, safe=False, status=404)
            
            data = []
            for producto in productos:
                linea = copy.deepcopy(request_data)
                linea.update(producto)
                linea.pop('productos')
                data.append(linea)
            
            for linea in data:
                try:
                    response = create_kit(None, db_name=db_name, request_data=linea)
                    print(response)
                    if response != 'created successfully':
                        return JsonResponse({'message': response}, safe=False, status=404)
                except Exception as e:
                    print(e)
                    return JsonResponse({'message': response}, safe=False, status=404)
                    
            if response == 'created successfully':
                print(response)
                return JsonResponse({'message': 'Kit created'}, safe=False, status=200)
            else:
                return JsonResponse({'message': response}, safe=False, status=404)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Error creating Kit'}, safe=False, status=404)

  # Update an Kit
    if request.method == 'PUT':

        try:
            request_data = dict(request.body)          
            productos=request_data.get('productos',None)
            
            if productos == None:
                return JsonResponse({'message': 'Field productos is required'}, safe=False, status=404)
            
            data = []
            for producto in productos:
                linea = copy.deepcopy(request_data)
                linea.update(producto)
                linea.pop('productos')
                data.append(linea)
            for linea in data:
                try:
                    response = update_kit(None, db_name=db_name, request_data=linea)
                    if response == 'Updated successfully':
                        return JsonResponse({'message': 'Kit updated'}, safe=False, status=200)
                
                except Exception as e:
                    print(e)
                    return JsonResponse({'message': 'Error updating Kit'}, safe=False, status=404)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Error updating Kit'}, safe=False, status=404)

 # Get storage by location
    if request.method == 'DELETE':

        productoean_pack = request.GET.get('productoean_pack', None)
        if productoean_pack == None:
            return JsonResponse({'error': 'Field productoean_pack is required'}, safe=False, status=404)
        
        try:
            response = delete_kit(productoean_pack, db_name=db_name)
            if response == 'Deleted successfully':
                return JsonResponse({'success': 'Kit deleted'}, safe=False, status=200)
            else:
                return JsonResponse({'message': response}, safe=False, status=404)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Error deleting Kit'}, safe=False, status=404)
