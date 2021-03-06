from .forms import TodoForm
from .models import Todo
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm


from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404


# Create your views here.
@method_decorator(login_required, name='dispatch')
class TodoListView(ListView):
    template_name = 'ToDo/todo_list.html'
    queryset = Todo.objects.all()


@method_decorator(login_required, name='dispatch')
class TodoDetailView(DeleteView):
    template_name = 'ToDo/todo_detail.html'
    queryset = Todo.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Todo, id=id_)


@method_decorator(login_required, name='dispatch')
class TodoCreateView(CreateView):
    template_name = 'ToDo/todo_create.html'
    form_class = TodoForm
    queryset = Todo.objects.all()


@method_decorator(login_required, name='dispatch')
class TodoUpdateView(UpdateView):
    template_name = 'ToDo/todo_create.html'
    form_class = TodoForm
    queryset = Todo.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Todo, id=id_)


@method_decorator(login_required, name='dispatch')
class TodoDeleteView(DeleteView):
    template_name = 'ToDo/todo_delete.html'
    #queryset = Todo.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Todo, id=id_)

    def get_success_url(self):
        return reverse('ToDo:todos')


# signup view
class SignUp(CreateView):
    template_name = 'ToDo/registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


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
