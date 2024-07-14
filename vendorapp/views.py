# vendorapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, VendorForm
from vendor.models import Product, Farmers
from categories.models import ProductCategory
from cart.models import *
@login_required(login_url='login')
def vendorform(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.farmer = request.user  # Set the farmer field to the logged-in user
            vendor.save()
            return redirect('products-upload')
    else:
        form = VendorForm()
    context = {'form': form}
    return render(request, 'vendorapp/vendorform.html', context)
 
@login_required(login_url='login')
def productsupload(request):
    # prod_cart = ProductCategory.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            try:
                farmer = Farmers.objects.filter(farmer=request.user).first()
                product.vendor = farmer
                product.save()
                return redirect('products-pages')
            except Farmers.DoesNotExist:
                # Handle the case where the farmer does not exist
                return redirect('vendorform')
    else:
        form = ProductForm()
    context = {'form': form, 
            #    'prod_cart': prod_cart
               }
    return render(request, 'vendorapp/index.html', context)


@login_required(login_url='login')
def product_pages(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    farmer = Farmers.objects.all()
    try:
        farmer = Farmers.objects.filter(farmer=request.user).first()
        products = Product.objects.filter(vendor=farmer)
    except Farmers.DoesNotExist:
        # Handle the case where the farmer does not exist
        products = []
    return render(request, 'vendorapp/products_page.html', {'products': products, 'vendors': farmer, 'cart': cart, 'cart_items': cart_items})

@login_required(login_url='login')
def check_vendor_status(request):
    try:
        Farmers.objects.get(farmer=request.user)
        return redirect('products-pages')  # Redirect to the product pages view if the user is a vendor
    except Farmers.DoesNotExist:
        return redirect('vendor-form')  # Redirect to the vendor registration form if the user is not a vendor
    
def activity(request):
    context = {}
    return render(request, 'vendorapp/activity_components.html', context)