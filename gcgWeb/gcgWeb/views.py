# filename: views.py (Django view functions)

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello from Micah!')

def home(request):
    return render(request, "templates/index.html")
