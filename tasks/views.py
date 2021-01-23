from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)

def update(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'update.html', context)

def delete(request, pk):
    item = Task.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    context = {'item': item}
    return render(request, 'delete.html', context)