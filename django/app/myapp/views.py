from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView


# Create your views here.


def home(request): 
    return render(request, 'home.html')


  
