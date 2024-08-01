from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Mateo Pineda'})

def about(request):
    return HttpResponse('<h1>Welcome to the About Page</h1>')