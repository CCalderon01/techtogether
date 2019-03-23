from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>home view</p>')

def questions(request, id):
    return HttpResponse('<p>questions view with the id{}</p>'.format(id))

def rating(request):
    return HttpResponse('<p>rating view</p>')

def recommendation(request, id):
    return HttpResponse('<p>recommendations view with the id{}</p>'.format(id))