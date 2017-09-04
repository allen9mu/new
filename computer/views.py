from django.shortcuts import render_to_response
from models import Computer

# Create your views here.

def list_coputer(request):
    list = Computer.objects.
