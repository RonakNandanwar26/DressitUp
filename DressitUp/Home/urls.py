from django.urls import path, include
from .views import home, contact, profile, about, list, shop
from products.views import productcreate

app_name = 'Home'

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('profile/edit/', profile, name='profile'),
    path('products/', include('products.urls', namespace='Products')),
]