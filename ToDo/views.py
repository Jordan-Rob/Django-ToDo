from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#from .models import Todo

def index(request):
    return HttpResponse("Todo app will be ready soon")

def todopost(request):
    return HttpResponse("Post Todo")