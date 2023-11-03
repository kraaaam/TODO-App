from django.shortcuts import render, redirect

from .models import TodoItem

# Create your views here.
def home(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'home.html', {'todo_items': todo_items})

def add_todo(request):
    if request.method == "POST":
        content = request.POST.get('content')
        TodoItem.objects.create(content=content)
    return redirect('home')
    
def delete_todo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return redirect('home')

def edit_todo(request, todo_id):
    if request.method == "POST":
        content = request.POST.get(f'content_{todo_id}')
        todo_item = TodoItem.objects.get(id=todo_id)
        todo_item.content = content
        todo_item.save()
    return redirect('home')