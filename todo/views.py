from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Todo

# Create your views here.
class CreateTodoView(View):
    template_name = 'index.html'
    def get(self, request):

        tasks_completed = Todo.objects.filter(completed = True)
        tasks_undone = Todo.objects.filter(completed = False)

        context = {
            'dones': tasks_completed,
            'undones': tasks_undone,
            'total': tasks_undone.count() + tasks_completed.count()
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request):
        todo = request.POST.get('todo')

        new_todo = Todo.objects.create(title=todo, completed=False)
        new_todo.save()

        return redirect('hello')
    
class EditTodoView(View):
    template_name = "edit.html"
    def get(self, request, task_id, *args, **kwargs):
        
        task = Todo.objects.get(id=task_id)

        context = {
            'task': task,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, task_id):

        #getting the new title
        new_title = request.POST.get('title')

        #getting the task we are modifying
        task = Todo.objects.get(id=task_id)

        #update the this task title
        task.title = new_title
        task.save()

        return redirect('hello')

class DeleteTodoView(View):
    template_name = 'delete.html'

    def get(self, request, task_id):
        task = Todo.objects.get(id=task_id)

        context = {
            'task': task,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, task_id):

        task = Todo.objects.get(id=task_id)

        task.delete()

        return redirect('hello')
    
class AcceptTodoView(View):
    template_name = 'index.html'
    def get(self, request):
        tasks_completed = Todo.objects.filter(completed = True)
        tasks_undone = Todo.objects.filter(completed = False)

        context = {
            'dones': tasks_completed,
            'undones': tasks_undone,
            'total': tasks_undone.count() + tasks_completed.count()
        }
        
        return redirect('hello')


    def post(self, request):
        if request.POST:
            dones = request.POST.getlist('dones[]')

            for done_id in dones:
                #get the id's of the done tasks
                done = Todo.objects.get(id=done_id)
                done.completed = True
                done.save()

        return redirect("hello")