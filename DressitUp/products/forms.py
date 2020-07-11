from django import forms
from .models import Product




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'gender', 'price', 'quantity', 'image1', 'image2', 'image3', 'image4', 'features']