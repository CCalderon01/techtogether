from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import FinalLocation, Location, Food, Transportation, Crime

def home(request):
    location = Location.objects.all()
    return render(request, 'html5up-eventually/index.html', {'location': location})

def questions(request, id):
    if question < 4:
        return render (request, 'question{}.html'.format(id), {'question': question})
    else:
        raise Http404('Question not found')

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