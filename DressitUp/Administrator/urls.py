from django.urls import path
from .views import *

app_name = 'Administrator'


urlpatterns = [
    path('', home, name='home'),
    path('Datatables',Datatables, name='Datatables')
]