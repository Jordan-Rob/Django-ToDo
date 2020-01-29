from django.urls import path

from .views import (
    TodoListView,
    TodoDetailView

)

app_name = "ToDo"

urlpatterns = [
    path('Todos/', TodoListView.as_view(), name='todos'),
    path('Todos/<int:id>/', TodoDetailView.as_view(), name='detail')

]
