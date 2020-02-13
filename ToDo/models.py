from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils import timezone
import datetime

# Create your models here.

"""class Users(models.Model):
    Full_names = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
"""


class TodoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Todo(models.Model):
    todolist = models.ForeignKey(
        TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='unamedTodo')
    description = models.CharField(max_length=200)
    Todo_date = models.DateTimeField('Todo Date')
    pub_date = models.DateTimeField('Date Published')

    def get_absolute_url(self):
        return reverse('ToDo:detail', kwargs={'id': self.id})

    def get_back_home(self):
        return reverse('ToDo:todos', kwargs={})

    def go_to_update(self):
        return reverse('ToDo:update', kwargs={'id': self.id})

    def go_to_delete(self):
        return reverse('ToDo:delete', kwargs={'id': self.id})

    # def __str__(self):
    #    return self.description

    """
    def create_todo(self, description, Todo_date, pub_date):
        todo = Todo(description=description,
                    Todo_date=Todo_date, pub_date=pub_date)
        todo.save()
        return todo

    def delete_todo(self, description):
        todo = Todo.objects.get(description=description)
        todo.delete()
        return "Todo removed"

    def clear_old_todo(self):
        todos = Todo.objects.all()
        time_limit = datetime.timedelta(hours=24)
        for todo in todos:
            if (timezone.now()-todo.pub_date) > time_limit:
                todo.delete()
                return "old todo cleared"
    """
