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


def detail(request, todo_description, todo_date, todo_pub_date):
    TodoDate = todo_date
    TodoDescription = todo_description
    publishDate = todo_pub_date
    template = loader.get_template('ToDo/detail.html')
    context = {
        'TodoDate': TodoDate,
        'TodoDescription': TodoDescription,
        'publishDate': publishDate
    }

    return HttpResponse(template.render(context, request))


def todopost(request):
    return HttpResponse("Post Todo")
