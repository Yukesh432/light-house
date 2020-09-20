from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Order
from django.http import HttpResponse


def light(request):
    product = Product.objects.filter(category= 1)
    context= {
        'products' : product
    }
    return render(request, 'products/lights.html', context) 

def switch(request):
    product = Product.objects.filter(category= 2)
    context= {
        'products' : product
    }
    return render(request, 'products/switchs.html', context)

def cable(request):
    product = Product.objects.filter(category= 3)
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

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address= request.POST.get('address_I', '') + " " + request.POST.get('address_II', '') 
      
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json =items_json, name=name, email=email, address=address, city=city, phone=phone)

        order.save()
        thank = True
        id = order.order_id
        return render(request, 'accounts/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'accounts/checkout.html') 