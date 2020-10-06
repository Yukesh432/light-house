from django.db import models
from products.models import Product, Category, Variation


class Cart(models.Model):

    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
    variations = models.ManyToManyField(Variation, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    notes = models.TextField(null= True, blank= True) 
    line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self):
        try:
            return str(self.cart.id)  
        except:
            return self.product.title
    def __str__(self):
        return self.product
      
