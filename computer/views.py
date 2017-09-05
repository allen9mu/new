from django.shortcuts import render, get_object_or_404
from .models import Computer

# Create your views here.

def list_coputer(request):
    list = Computer.objects.order_by('date_added')
    return render(request, 'computer/list.html',{'list':list})


    
