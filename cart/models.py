# cart/models.py
from django.db import models
from django.contrib.auth.models import User
from vendor.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart({self.user.username})'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)
    cart_price = models.DecimalField(max_digits=10, decimal_places=2, default=1)

    def save(self, *args, **kwargs):
        self.cart_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return f'CartItem({self.product.name} x {self.quantity})'
    
    #Movie name: My Spy
    

    