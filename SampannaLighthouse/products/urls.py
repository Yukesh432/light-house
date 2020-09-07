from django.urls import path
from . import views

urlpatterns= [
    
    path('lights', views.light, name= 'light'),
    path('cables', views.cable, name= 'cable'),
    path('switchs', views.switch, name= 'switch'),
    path('gadgets', views.gadget, name= 'gadget'),
    path('productview', views.productview, name= 'productview'),
    path('dummy/<username>/', views.dummy, name= 'dummy'),
    
 
]  