from django.shortcuts import render
from products.models import Product, Category
from django.http import HttpResponse



def index(request):
    products= Product.objects.order_by('-list_date').filter(is_published= True)[:5]
    context= {
        'products': products,
        
    }
    return render(request, 'pages/index.html', context)


def about(request):
    
    return render(request, 'pages/about.html')
def contact(request):
    
    return render(request, 'pages/contact.html')
def termscondition(request):
    
    return render(request, 'pages/termscondition.html')
def returnpolicy(request):
    
    return render(request, 'pages/returnpolicy.html')
