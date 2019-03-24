from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from django.views.generic import TemplateView
from .models import FinalLocation, Location, Food, Transportation, Crime
from airbnbtech.forms import HomeForm



def home(request):
    if request.method == 'POST':
        url = request.POST.get("url", "")
        airbnb_url = url.split('/')[4].split("?")[0]
        print(airbnb_url)

    return render(request, 'index.html', {})
    # location = Location.objects.all()
    # return render(request, 'index.html')

def form(request):
    return render (request, 'form.html')

def rating(request):
    return render(request, 'rating.html')

def recommendation(request, id):
    food = Food.objects.all()
    transportation = Transportation.objects.all()
    crime = Crime.objects.all()
    final_location = FinalLocation.obects.all()
    return HttpResponse('<p>recommendations view with the id{}</p>'.format(id))
