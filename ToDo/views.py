from .forms import TodoForm
from .models import Todo

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


# Create your views here.

class TodoListView(ListView):
    template_name = 'ToDo/todo_list.html'
    queryset = Todo.objects.all()


class TodoDetailView(DeleteView):
    template_name = 'ToDo/todo_detail.html'
    queryset = Todo.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Todo, id=id_)


"""
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


def todo_delete(request, todo_description):
    todo = Todo.objects.get(description=todo_description)
    todo.delete()
    return redirect('Todo/index.html')


def todopost(request):
    return HttpResponse("Post Todo")
"""
