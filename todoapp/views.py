from django.http import request
from django.shortcuts import render

from todoapp.models import Todo

# Create your views here.


def homeView(request):
    todo_list = Todo.objects.all()
    return render(request,'home.html',{'todo_list': todo_list})
