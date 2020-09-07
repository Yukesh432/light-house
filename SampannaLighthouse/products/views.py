from django.shortcuts import render
from .models import Cable, Switch, Light


def light(request):
    lights= Light.objects.order_by('-list_date').filter(is_published= True)
    context= {
        'lights': lights
    } 
   
    return render(request, 'products/lights.html', context)

def cable(request):
    cables= Cable.objects.order_by('-list_date').filter(is_published= True)
    context= {
        'cables': cables
    } 
    return render(request, 'products/cables.html', context)

def switch(request):
    switchs= Switch.objects.order_by('-list_date').filter(is_published= True)
    context= {
        'switchs': switchs
    } 
    return render(request, 'products/switchs.html', context)

def gadget(request):
    return render(request, 'products/gadgets.html')

def productview(request):
    return render(request, 'products/productview.html')

def dummy(request, username):
    return render(request, 'products/dummy.html')