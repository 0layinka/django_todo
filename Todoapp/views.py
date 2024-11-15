from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.

def home(request):
    todo = Todo.objects.all()
    data = {
        'todo': todo
    }
    return render(request, 'home.html', data)
   

def create(request,):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = TodoForm
        context = {
            'form': form
        }
        return render(request, 'create.html', context)


def read(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        'todo': todo
    }
    return render(request, 'read.html', context)


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = TodoForm(instance=todo)
        context = {
            'form': form,
            'todo': todo
        }
        return render(request, 'update.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect(home)
    else:
        return render(request, 'delete.html')