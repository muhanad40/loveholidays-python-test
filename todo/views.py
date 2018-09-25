from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from .models import Todo

class TodoView(TemplateView):

  template_name = "todo/index.html"

  def get_context_data(self, **kwargs):
    context = super(TodoView, self).get_context_data(**kwargs)
    context['tasks'] = Todo.objects.all()
    return context

  def post(self, request, **kwargs):
    task = request.POST
    new_todo = Todo(description=task.get('description'), is_complete=False)
    new_todo.save()
    return redirect('home')

def RemoveTodo(request, id):
  task = Todo.objects.get(id=id)
  task.delete()
  return redirect('home')

def CompleteTodo(request, id):
  task = Todo.objects.get(id=id)
  task.is_complete = True
  task.save()
  return redirect('home')

def IncompleteTodo(request, id):
  task = Todo.objects.get(id=id)
  task.is_complete = False
  task.save()
  return redirect('home')
