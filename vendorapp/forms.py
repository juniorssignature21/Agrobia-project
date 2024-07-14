# vendorapp/forms.py
from django.forms import ModelForm
from vendor.models import Product, Farmers

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['vendor']
        

class VendorForm(ModelForm):
    class Meta:
        model = Farmers
        fields = '__all__'
        exclude = ['farmer']
        

