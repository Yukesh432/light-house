from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cart, CartItem
from products.models import Product, Category, ProductImage, Variation
from django.contrib.auth.models import User



def cart(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id = the_id)

    except:
        the_id = None 
    if the_id:
         
        new_total = 0.00
        # each_tot= cart.cart_item.quantity * product.price
        # print(each_tot)
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
       
        request.session['items_total'] = cart.cartitem_set.count()
        # print(cart.products.count())
        cart.total = new_total
        cart.save()
        context = { 
        'cart': cart
        }
    else:
        empty_message = "Your cart is empty, please keep shopping"
        context = {"empty": True, 'empty_message': empty_message}

   
     
    return render(request, 'carts/cart.html', context) 
 

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        # print("bookkkkkkkkkkkk")
        cart = Cart.objects.get(id = the_id)
 
    # print(cart)
        
    except:
        return redirect(reverse('cart')) 
    
    cartitem = CartItem.objects.get(id= id)

    print(cartitem)
    # cartitem.delete()
    cartitem.cart = None
    cartitem.save()
    #send success messgae
    return redirect(reverse('checkout'))
        



def add_to_cart(request, title):
    if request.user.is_authenticated:
    
        print(" logged in ")
        request.session.set_expiry(20000000)
    else:
        print("not logged in ")
        request.session.set_expiry(10)

    try:
        the_id = request.session['cart_id']


    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id = the_id)

    
    try:
        product = Product.objects.get(title= title)
    except Product.DoesNotExist:
        pass
    except: 
        pass
    
    product_var= []  #product variation
    if request.method == 'POST':
        qty= request.POST['qty']
        for item in request.POST: 
            key = item
            val= request.POST[key]
            # print(key, val)
            try:
                v= Variation.objects.get(product= product, category__iexact= key, title__iexact= val)
                product_var.append(v)
            except:
                pass
        cart_item = CartItem.objects.create(cart= cart, product= product)
        print("bommmmmm")
        # print(cart_item)
        if len(product_var)>0:
            cart_item.variations.add(*product_var)
        cart_item.quantity = qty
        cart_item.save()

        # success message
        return redirect(reverse('cart'))
    return redirect(reverse('cart'))
    
