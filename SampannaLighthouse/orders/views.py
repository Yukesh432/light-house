from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from carts.models import Cart
from .models import Order
import time
from .utils import id_generator



def orders(request):
    return render(request, "carts/user.html")


@login_required
def checkout(request):
    
    try:
        the_id = request.session['cart_id']
        cart= Cart.objects.get(id= the_id)

    except:
        the_id = None
        return redirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart= cart)

    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user =  request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        return redirect(reverse("cart"))





    if new_order.status == "Finished":
        del request.session['cart_id']
        del request.session['items_total']
        return redirect(reverse("cart"))


    
    context = {

    }



    return render(request, "carts/checkout.html", context) 