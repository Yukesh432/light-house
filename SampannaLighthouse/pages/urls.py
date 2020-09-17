from django.urls import path
from . import views

urlpatterns= [
    
    path('', views.index, name= 'index'),
    path('about', views.about, name= 'about'),
    path('contact', views.contact, name= 'contact'),
    path('termscondition', views.termscondition, name= 'termscondition'),
    path('returnpolicy', views.returnpolicy, name= 'returnpolicy'),
]  