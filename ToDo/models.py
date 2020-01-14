from django.db import models

# Create your models here.

"""class Users(models.Model):
    Full_names = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
"""


class Todo(models.Model):
    description = models.CharField(max_length=200)
    Todo_date = models.DateTimeField('Todo Date')

    def __str__(self):
        return self.description

    def create_todo(self, description, Todo_date):
        todo = Todo(description=description, Todo_date=Todo_date)
        todo.save()
        return todo

    def delete_todo(self, description):
        todo = Todo.objects.get(description=description)
        todo.delete()
        return "Todo removed"
