from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from vendor.models import Product
from categories.models import ProductCategory
from django.contrib.auth.models import User
from cart.models import *


# def home(request):
#     return render(request, 'store/home.html')

# store/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .forms import SignUpForm

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("you have registered successfully!!!"))
            return redirect("home")
        else:
            messages.success(request, ("there was a problem registering!!!"))
            return redirect("register")
    else:
        return render(request, 'store/register.html', {"form": form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been Logged in successfully!!!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error please try again!!!"))
            return redirect('home')
    else:
        return render(request, 'store/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("you have been logged out!!!"))
    return redirect('home')

@login_required
def user_details(request):
    user = request.user  # Get the currently logged-in user
    context = {
        'username': user.username,
        'email': user.email,
        # 'phone': user.phone,
        # Add any other user details you want to return
    }
    return render(request, 'store/user_profile.html', context)

def product_section(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    product = Product.objects.all()[:6]
    categories = ProductCategory.objects.all()
    context = {'product': product, 'categories': categories,
               'cart': cart,
            'cart_items': cart_items}
    return render(request, 'store/home.html', context)

# def user_img(request):
#     form = UserImg()
#     if request.method == 'POST':
#         form = UserImg(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context={'form': form}
#     return render(request, 'store/image-upload.html', context)
    
