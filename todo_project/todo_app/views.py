from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from todo_app.models import ToDoItems
from django.utils import timezone

# Create your views here.

def index(request):
    created_todo = ToDoItems.objects.all().order_by('-added_date')
    return render(request,'todo_app/index.html',{'created_todo':created_todo})

def details(request):
    todo_item =request.POST['todo_item'] 
    date_added = timezone.now()
    created_todo= ToDoItems.objects.create(added_date=date_added,text=todo_item,)
    print(created_todo.text)
    return HttpResponseRedirect('/todo_app')

def delete_todo(request,todo_id):
    ToDoItems.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todo_app')
