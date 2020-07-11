from django.shortcuts import render
from .models import Amenities
from .forms import Amenities_form
# Create your views here.


def Show_Amenities_view(request):
    temp = '#'
    if request.method == "POST":
        form = Amenities_form(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, temp, {'show_Amenities_form':form})



    # temp = '#'
    # is_Amenities = Amenities.objects.all()
    # if is_Amenities:
    #     data = Amenities.objects.all()
    # return render(request, temp, {'data':data})





        # if form.is_valid():
        #     Amenities_name = form.cleaned_data['name']
        #     form.save()
        # else:
        #     form = Amenities_form