from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
import products
from .forms import ProductForm
from Home.forms import ProfileForm
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.list import ListView
# Create your views here.


@login_required
def productcreate(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST or None, request.FILES or None)
        if product_form.is_valid():
            f = product_form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Product Added Successfully..')
            return redirect('Home:home')
        else:
            messages.error(request, 'failed to add Product')
    else:
        product_form = ProductForm()
    template = 'Home/createproduct.html'
    return render(request, template, {'product_form': product_form})


def insert(request):
    image = request.FILES['image']
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    uploaded_file_url = fs.url(filename)
    p = Product()
    p.image = uploaded_file_url


# RentProducts Cloths ListView
# class productslist(LoginRequiredMixin, ListView):
#     login_url = '/accounts/login/'
#     # redirect_field_name = 'next'
#     # paginate_by = 10
#     template_name = 'Home/list.html'

    # def get(self, request, *args, **kwargs):
    #     object_list = Product.objects.filter(product_for='rent').filter(type__iexact='cloths').order_by("-timestamp")
    #     filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    #     current_order_projects = []
    #
    #     page = request.GET.get('page', 1)
    #     paginator = Paginator(object_list, 10)
    #     try:
    #         object_list = paginator.page(page)
    #     except PageNotAnInteger:
    #         object_list = paginator.page(1)
    #     except EmptyPage:
    #         object_list = paginator.page(paginator.num_pages)
    #
    #     if filtered_objects.exists():
    #         user_order = filtered_objects[0]
    #         user_order_items = user_order.items.all()
    #         current_order_projects = [product.product for product in user_order_items]
    #
    #     return render(request, self.template_name, {
    #         'object_list': object_list,
    #         'current_order_projects': current_order_projects
    #     })



def productslist(request):
    products = Product.objects.all()
    template = 'Home/list.html'
    return render(request, template, {'products': products})


def Men(request):
    products = Product.objects.filter(gender='Male')
    template = 'Category/Men.html'
    return render(request, template, {'products': products})


def singleproduct(request, pk):
    template = 'Home/singleproduct.html'
    return render(request, template, {'products': products})



def editproduct(request, pk):
    template = 'Home/add_product.html'
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product Updated Successfully..')
        return redirect('Home:home')
    return render(request, template, {'form': form})


def deleteproduct(request, pk):
    template = 'Home/deleteproduct.html'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully..')
        return redirect('Home:home')
    return render(request, template, {})




