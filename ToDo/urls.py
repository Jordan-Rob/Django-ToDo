from django.urls import path

from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView

)

app_name = "ToDo"

urlpatterns = [
    path('Todos/', TodoListView.as_view(), name='todos'),
    path('Todos/<int:id>/', TodoDetailView.as_view(), name='detail'),
    path('Todos/create/', TodoCreateView.as_view(), name='create')

]
