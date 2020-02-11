from django.urls import path

from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,

)

app_name = "ToDo"

urlpatterns = [
    path('Todos/', TodoListView.as_view(), name='todos'),
    path('Todos/<int:id>/', TodoDetailView.as_view(), name='detail'),
    path('Todos/create/', TodoCreateView.as_view(), name='create'),
    path('Todos/<int:id>/update/', TodoUpdateView.as_view(), name='update'),
    path('Todos/<int:id>/delete/', TodoDeleteView.as_view(), name='delete'),
    # path('login/', , name='login'),
    # path('register/', , name='register')

]
