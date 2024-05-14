from django.shortcuts import render

from .models import Task

def show_task(response):
    return render(response, 'task/task.html')
