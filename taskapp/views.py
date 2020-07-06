from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'taskapp/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.created_date = timezone.now()
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'taskapp/task_add.html', { 'form': form })

#def task_update(request, pk):

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')
