
from django.shortcuts import render
from todo_list.models import Task


def home( request):
    tasks=Task.objects.filter(is_completed=False)
    completed_tasks=Task.objects.filter(is_completed=True)
    context={
        'tasks':tasks,
        'completed_tasks': completed_tasks
    }
    return render(request,'home.html', context)