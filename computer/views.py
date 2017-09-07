from django.shortcuts import render, get_object_or_404
from .models import Computer
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ComputerForm

# Create your views here.

def list_computer(request):
    list = Computer.objects.order_by('date_added')
    return render(request, 'computer/list.html',{'list':list})

def add_computer(request):
    if request.method !='POST':
        form = ComputerForm()
    else:
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("computer:list_computer"))
    
    context = {'form': form}
    return render(request,'computer/add.html',context)


def index(request):
    list = Computer.objects.order_by('date_added')
    if request.method !='POST':
        form = ComputerForm()
    else:
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("computer:index"))
    
    context = {'form': form}
    return render(request,'computer/index.html',{'form': form,'list':list} )