from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# todo/views.py
def addTask(request):
  task=request.POST['task']
  Task.objects.create(task=task)
  return redirect('home')