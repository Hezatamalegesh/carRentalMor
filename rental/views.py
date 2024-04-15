from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html.jinja')

def index(request):
    return render(request, 'cars.html.jinja')

def index(request, car_id):
    return render(request, 'car.html.jinja')