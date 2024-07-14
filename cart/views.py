# from django.shortcuts import render, get_object_or_404
# from .cart import Cart
# from vendor.models import Product
# from django.http import JsonResponse

# # Create your views here.

# def cart_summary(request):
#     # Cart
#     cart = Cart(request)
#     cart_products = cart.get_products()
#     quantities = cart.get_quants
#     totals = cart.cart_total
#     return render(request, "cart/shopping_cart.html", {'cart_products': cart_products, 'quantities': quantities, 'totals': totals})


# def cart_add(request):
#     # Get the cart
#     cart = Cart(request)
#     #test for post
#     if request.POST.get('action') == 'post':
#         #Get stuff 
#         product_id = int(request.POST.get('product_id'))
#         product_qty = int(request.POST.get('product_qty'))

#         # lookup product in the database
#         product = get_object_or_404(Product, id=product_id)

#         # save to a section
#         cart.add(product=product, quantity=product_qty)

#         #get cart quantity
#         cart_quantity = cart.__len__()

#         #return response
#         # response = JsonResponse({'Product Name: ': product.name})
#         response = JsonResponse({'qty': cart_quantity}) 
#         return response


# def cart_delete(request):
#     cart = Cart(request)

#     if request.POST.get('action') == 'post':
#         #Get stuff 
#         product_id = int(request.POST.get('product_id'))

#         cart.delete(product=product_id)
        
#         response = JsonResponse({'product': product_id})
#         return response

   
# def cart_update(request):
#     cart = Cart(request)

#     if request.POST.get('action') == 'post':
#         #Get stuff 
#         product_id = int(request.POST.get('product_id'))
#         product_qty = int(request.POST.get('product_qty'))

#         cart.update(product=product_id, quantity=product_qty)

#         response = JsonResponse({'qty': product_qty})
#         return response


# cart/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from vendor.models import Product

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    # context = {
    #     'cart': cart,
    #     'created': created,
    #     'cart_item': cart_item
    # }
    return redirect(to='cart_detail')
    

@login_required(login_url='login')
def cart_detail(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        context = {
            'cart': cart,
            'cart_items': cart_items
        }
        return render(request, 'cart/cart_detail.html', context)
    except:
        return redirect('null-cart')

@login_required(login_url='login')
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    
    if cart_item.quantity >= 1:
        cart_item.quantity -= 1
        cart_item.delete()
        return redirect('cart_detail')
        
            
 
        # cart_item.save()
    # else:

def decrease_cart_quantity(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    
    if cart_item.quantity > 0:
        cart_item.quantity -= 1
        if cart_item.quantity == 0:
            cart_item.delete()
        else:
            cart_item.save()
    return redirect('cart_detail')

def increase_cart_quantity(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    
    cart_item.quantity += 1
    if cart_item.quantity > product.stock:
        cart_item.quantity -= 1
        # return redirect('/')
    cart_item.save()
    return redirect('cart_detail')
    


@login_required(login_url='login')
def null_cart(request):
    return render(request, 'cart/null_cart.html')


@login_required(login_url='login')
def update_cart_quantity(request, product_id, action):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product
                                                        , user=request.user)

    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()

    return HttpResponse(('cart_item_partial.html', {'item': cart_item}))

