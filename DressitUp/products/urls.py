from django.urls import path, include
from .views import *

app_name = 'products'

urlpatterns = [
    path('list/', productslist, name='products_list'),
    path('edit/<int:pk>/', editproduct, name='product_edit'),
    path('delete/<int:pk>/', deleteproduct, name='product_delete'),
    path('productcreate/', productcreate, name='product_create'),
    path('singleproduct/<int:pk>/', singleproduct, name='product_single'),
    path('Men/', Men, name='product_Men')
]