from django.shortcuts import render
from products.models import Product, Category

def index(request):
    
    return render(request, 'pages/index.html')
def about(request):
    
    return render(request, 'pages/about.html')
def contact(request):
    
    return render(request, 'pages/contact.html')
