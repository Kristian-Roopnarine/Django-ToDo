from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details',views.details,name='details'),
    path('delete_todo/<int:todo_id>/',views.delete_todo,name='delete')
]