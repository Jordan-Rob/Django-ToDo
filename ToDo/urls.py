from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.todopost, name='post')
]
