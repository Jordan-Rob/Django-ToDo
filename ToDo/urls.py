from django.urls import path

from . import views

app_name = "ToDo"

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<todo_description>', views.detail, name='detail'),
    path('post', views.todopost, name='post')
]
