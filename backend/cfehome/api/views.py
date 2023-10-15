from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def api_home(request, *args, **kwargs):
    # request is not from python module it is django request
    # request.body
    
    print(request.GET)
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of json data -> Python Dict
    except:
        pass
    # data['headers'] = request.headers # request.META
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers) # request.META
    data['content_type'] = request.content_type # request.META
    return JsonResponse(data)