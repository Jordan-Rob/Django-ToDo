from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Todo


def index(request):
    latest_todos = Todo.objects.order_by('-pub_date')
    output = ', '.join([todo.description for todo in latest_todos])
    return HttpResponse(output)


def detail(request, todo_description):
    return HttpResponse("Details of Todo {}".format(todo_description))


def todopost(request):
    return HttpResponse("Post Todo")
