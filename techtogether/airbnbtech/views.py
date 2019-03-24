from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from django.views.generic import TemplateView
from .models import FinalLocation, Location, Food, Transportation, Crime
from airbnbtech.forms import HomeForm



def home(request):
    if request.method == 'POST':
        url = request.POST.get("url", "")
        airbnb_id = url.split('/')[4].split("?")[0]
        print(airbnb_id)
        return render(request, 'djmaps/maps/templates/explore.html')
        # return render(request, 'rating.html', {'airbnb_id':airbnb_id, 'location':Location.objects.get(id=airbnb_id)})

    return render(request, 'rating.html', {})

def form(request):
    return render (request, 'form.html')

def rating(request):
    return render(request, 'rating.html')

def recommendation(request, id):
    # food = Food.objects.all()
    # transportation = Transportation.objects.all()
    # crime = Crime.objects.all()
    # final_location = FinalLocation.obects.all()

    return render(request, 'djmaps.maps.templates.explore.html')
