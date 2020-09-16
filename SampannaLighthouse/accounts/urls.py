from django.urls import path
from . import views

urlpatterns= [
    
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('checkout/', views.checkout, name= 'checkout'),
    path('profile/', views.profile, name= 'profile'),
    path('logout/', views.logout, name= 'logout'),
    path('recovery/', views.recovery, name= 'recovery'),

]  