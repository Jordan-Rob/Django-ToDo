from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.detail, name='detail'),
    path('post', views.todopost, name='post')
]
