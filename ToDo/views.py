from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import Todo


def index(request):
    latest_todos = Todo.objects.order_by('-pub_date')
    template = loader.get_template('ToDo/index.html')
    context = {
        'latest_todos': latest_todos
    }
    return HttpResponse(template.render(context, request))


def detail(request, todo_description):
    return HttpResponse("Details of Todo {}".format(todo_description))


def todopost(request):
    return HttpResponse("Post Todo")
