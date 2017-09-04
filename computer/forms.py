

from django import forms
from .models import     Computer

class ComputerForm(forms.Form):
    class Meta:
        model = Computer
        files = {'owner'}
    