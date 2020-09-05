from django.shortcuts import render


def light(request):
    return render(request, 'products/lights.html')

def cable(request):
    return render(request, 'products/cables.html')

def switch(request):
    return render(request, 'products/switchs.html')

def gadget(request):
    return render(request, 'products/gadgets.html')

def productview(request):
    return render(request, 'products/productview.html')