from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    TodoDate = Todo.objects.get(description=todo_description).Todo_date
    TodoDescription = todo_description
    publishDate = Todo.objects.get(description=todo_description).pub_date
    template = loader.get_template('ToDo/detail.html')
    context = {
        'TodoDate': TodoDate,
        'TodoDescription': TodoDescription,
        'publishDate': publishDate
    }

    return HttpResponse(template.render(context, request))


def delete_todo(request, todo_description):
    todo = Todo.objects.get(description=todo_description)
    todo.delete_todo(description=todo_description)
    template = loader.get_template('Todo/detail.html')
    return HttpResponseRedirect(template)


def todopost(request):
    return HttpResponse("Post Todo")
