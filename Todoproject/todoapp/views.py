from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class listview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task1'

class detailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'tasks'

class updateview(UpdateView):
    model=task
    template_name = 'edit.html'
    context_object_name = 'tasks'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')


# Create your views here.
def add(request):
    task1=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        tasks=task(name=name,priority=priority,date=date)
        tasks.save()
    return render(request,'home.html',{'task1':task1})

def delete(request,taskid):
    task2=task.objects.get(id=taskid)
    if request.method=='POST':
        task2.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    task3=task.objects.get(id=id)
    form=todoform(request.POST or None, instance=task3)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task3':task3})

