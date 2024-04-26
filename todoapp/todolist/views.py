from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/index.html', {'todo_list': todos,
                                                   'title': 'Главная страница',
                                                   })


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = Todo(title=title)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.is_complete = todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')
