from django.shortcuts import render

# Create your views here.

def home(request):
    template = 'Administrator/index.html'
    return render(request, template, {})


def Datatables(request):
    template = 'Administrator/datatables.html'
    return render(request, template, {})