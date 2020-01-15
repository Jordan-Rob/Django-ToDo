from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#from .models import Todo


def index(request):
    return HttpResponse("Todo app will be ready soon")


def detail(request, todo_description):
    return HttpResponse("Details of Todo {}".format(todo_description))


def todopost(request):
    return HttpResponse("Post Todo")
