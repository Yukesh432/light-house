from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from carts.models import Cart
from django.conf import settings

User= get_user_model()


STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)



class Order(models.Model):
    # order_id = models.CharField(max_length=120, default="ABC", unique=True)
    # cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    # status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    # user = models.ForeignKey(User, blank=True, null= True, on_delete= models.SET_NULL)
    user = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=120, blank=True)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120, blank=True)
    address_description = models.TextField(blank=True)
    phone = models.CharField(max_length=10, blank=True)
    # final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)

    
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)    
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return str(self.address)
