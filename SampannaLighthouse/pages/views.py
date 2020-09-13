from django.shortcuts import render
from products.models import Product, Category

def index(request):
    
    return render(request, 'pages/index.html')
