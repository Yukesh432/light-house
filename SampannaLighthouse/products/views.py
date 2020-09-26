from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import HttpResponse


def light(request):
    product = Product.objects.filter(category= 1)
    context= {
        'products' : product
    }
    return render(request, 'products/lights.html', context) 

def switch(request):
    product = Product.objects.filter(category= 3)
    context= {
        'products' : product
    }
    return render(request, 'products/switchs.html', context)

def cable(request):
    product = Product.objects.filter(category= 2)
    context= {
        'products' : product 
    }
    return render(request, 'products/cables.html', context)

def gadget(request):
    product = Product.objects.filter(category= 4)
    
    
    context= {
        'products' : product,
        
    }
    return render(request, 'products/gadgets.html', context)

def productview(request, product_id):
    # product = Product.objects.all()

    # product= [gadget1, switch]
    product= Product.objects.get(id= product_id)
    # product2 = Product.objects.get(title= product_title)
    

    # switch= Switch.objects.get(id= product_id)
    context = {
        'product' : product,
        # 'product2' : product2, 
      
    }
    return render(request, 'products/productview.html', context)

def cate(request):
    return render(request, 'products/category.html')


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q= None
    if q:
        products= Product.objects.filter(title__icontains= q)
        productsAdd = Product.objects.filter(details__icontains= q)
        context = {'query': q, 'products': products, 'productsAdd': productsAdd}
    else:
        context = {}
    return render(request, 'products/result.html', context)
