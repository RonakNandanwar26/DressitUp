from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, ProfileForm, UserForm
from django.contrib import messages
from django.core.mail import send_mail
from DressitUp import settings
from products.forms import ProductForm


# Create your views here.
def home(request):
    template = 'Home/index.html'
    return render(request, template, {})


def list(request):
    template = 'Home/list.html'
    return render(request, template, {})


def about(request):
    template = 'Home/about.html'
    return render(request, template, {})


def shop(request):
    template = 'Home/shop.html'
    return render(request, template, {})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            content = form.cleaned_data['message']
            print(contact_name)
            form.save()
            subject = 'Hello ' + contact_name + ' from DressitUp!'
            message = 'Stay Connected. We would love to hear you!'
            email_from = settings.EMAIL_HOST_USER
            email_to = [contact_email, ]
            send_mail(subject, message, email_from, email_to)
            messages.success(request, 'Form submitted successfully.')
            return redirect('Home:home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ContactForm()
    template = 'Home/contact.html'
    return render(request, template, {'form': form})


def profile(request):
    template = 'Home/profile.html'
    if request.method == 'POST':
        user_form = UserForm(request.POST or None, request.FILES or None, instance=request.user)
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your Profile is Updated Successfully..")
            return redirect('Home:home')
        else:
            messages.error(request, 'Please Correct the error below')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, template, {'user_form': user_form,
                                      'profile_form': profile_form})



