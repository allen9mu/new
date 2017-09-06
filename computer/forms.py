

from django import forms
from .models import     Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['owner','date_made','company_name','computer_model']
        #labels = {'owner':'' }
        
    