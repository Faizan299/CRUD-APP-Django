from pickle import TRUE
from django.shortcuts import render
from django.http import JsonResponse


def get_data(request):
    get =  {
        'success'  : True,
        'message'  : 'Function based view api to get data'
    }

    return JsonResponse(get)

def create_data(request):
    if request.method == 'POST':
        create = {
            'success' : True,
            'message' : 'Function bases view api to create data'
        }
    else:
        create1 = {
            'success': False,
            'message' : 'Function bases view : Invalid request'
        }
        return JsonResponse(create1)

def update_data(request):
    if request.method == 'PUT':
        update = {
            'success' : True,
            'message'  : 'Function based view api to update data'
        }
    
    else:
        update1 = {
            'success' : False,
            'message'  : 'Function based view : Invalid request'
        }
    return JsonResponse(update1)
        


