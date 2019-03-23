from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from django.views.generic import TemplateView
from airbnbtech.forms import HomeForm

from .models import FinalLocation, Location, Food, Transportation, Crime

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):


def home(request):
    location = Location.objects.all()
    return render(request, 'index.html', {'location': location})

def form(request):
    return render (request, 'form.html')

def rating(request):
    food = Food.objects.all()
    transportation = Transportation.objects.all()
    crime = Crime.objects.all()
    return HttpResponse('<p>rating view</p>')

def recommendation(request, id):
    food = Food.objects.all()
    transportation = Transportation.objects.all()
    crime = Crime.objects.all()
    final_location = FinalLocation.obects.all()
    return HttpResponse('<p>recommendations view with the id{}</p>'.format(id))
