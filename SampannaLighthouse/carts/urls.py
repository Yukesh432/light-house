from django.urls import path

from . import  views


urlpatterns= [
    
    # path('checkout/', views.checkout, name= 'checkout'),
    # path('productview/', views.productview, name= 'dummy'),
    path('cart/', views.cart, name= 'cart'), 
    path('cart/<str:title>/', views.add_to_cart, name= 'add_to_cart'),
    path('cart/<int:id>/', views.remove_from_cart, name= 'remove_from_cart'),
 
    

]  
      