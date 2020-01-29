from django.urls import path

from .views import TodoListView

app_name = "ToDo"

urlpatterns = [
    path('Todos/', TodoListView.as_view(), name='todos'),

]
