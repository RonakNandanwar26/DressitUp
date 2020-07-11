from django import forms
from .models import Contact, Profile
from django.contrib.auth.models import User
from products.forms import ProductForm
from products.models import Product


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20,disabled=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50, disabled=True)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'address', 'tel', 'gender', 'age', 'file')


