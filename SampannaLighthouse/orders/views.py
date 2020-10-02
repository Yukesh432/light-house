from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from carts.models import Cart
from .models import Order
import time
from .utils import id_generator


@login_required
def checkout(request): 
    if request.method == "POST":
        user_username = request.POST.get('user_username')
        email = request.POST.get('email')
        city = request.POST.get('city')
        address = request.POST.get('address_I')
        address2 = request.POST.get('address_II')
        address_description = request.POST.get('address_description')
        phone = request.POST.get('phone')

        # the_id = request.session['cart_id']
        # cart= Cart.objects.get(id= the_id)
        order = Order(user=user_username, email=email, address= address, address2=address2, address_description=address_description, city=city, phone=phone)
        order.save()
        return redirect("/")
        


    try:
        the_id = request.session['cart_id']
        cart= Cart.objects.get(id= the_id)

    except:
        the_id = None
        return redirect(reverse("cart"))

    # try:
    #     new_order = Order.objects.get(cart= cart)

    # except Order.DoesNotExist:
    #     new_order = Order()
    #     new_order.cart = cart
    #     new_order.user =  request.user
    #     new_order.order_id = id_generator()
    #     new_order.save()
    # except:
    #     return redirect(reverse("cart"))


    #adding products on final bill
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id = the_id)

    except:
        the_id = None 
    if the_id:
         
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
            # print("hohohoho")
  

        request.session['items_total'] = cart.cartitem_set.count()
        # print(cart.products.count())
        cart.total = new_total
        cart.save()
        context = { 
        'cart': cart
        }
    else:
        print("dodododdododododod..............")

    return render(request, 'carts/checkout.html', context) 
 
    # if new_order.status == "Finished":
    #     del request.session['cart_id']
    #     del request.session['items_total']
    #     return redirect(reverse("cart"))


    
    context = {
    }
    
    return render(request, "carts/checkout.html", context) 

























# def orders(request):
    
    # if request.method == "POST":
    
    # return render('/')

        # username = request.POST('name')
        # email = request.POST('email')
        # city = request.POST('city')
        # address = request.POST('address_I')
        # address2 = request.POST('address_II')
        # address_description = request.POST('address_description')
        # phone = request.POST('phone')

        # the_id = request.session['cart_id']
        # cart= Cart.objects.get(id= the_id)

        # order_id= id_generator()

        # order = Order(email=email, address= address, address2=address2, address_description=address_description, city=city, phone=phone)
        # order.save()
        # print("not now plaeasedsdsff d fdf dfd ")
        # print(cart)

        # if order.status == "Finished":
        #     del request.session['cart_id']
        #     del request.session['items_total']
        #     return redirect(reverse("cart"))
        
    #     return redirect("/")

    # else:
    #     return render(request, 'accounts/register.html')
