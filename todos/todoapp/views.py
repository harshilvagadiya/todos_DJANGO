from django.shortcuts import redirect, render
from .models import myTodo
from .forms import toDoForms

# Create your views here.
def allTodos(request):
    task = myTodo.objects.all()
    form = toDoForms()
    if request.method == 'POST':
        form = toDoForms(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request, 'all_todos.html', {"task": task, "form": form})

def delete_items(request, pk):
    task = myTodo.objects.get(pk=pk)
    task.delete()
    return redirect('allTodos')

def update_items(request, pk):
    todo = myTodo.objects.get(pk=pk)
    update_form = toDoForms(instance = todo)
    if request.method == 'POST':
        update_form = toDoForms(request.POST, instance = todo)
        if update_form.is_valid():
            update_form.save()
            return redirect('allTodos')
    return render(request, 'updateitems.html', {'todo': todo, "update_form": update_form })

    