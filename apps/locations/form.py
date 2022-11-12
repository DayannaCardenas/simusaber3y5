from django import forms
from apps.locations.models import*

class OfficeForm(forms.ModelForm):
    class Meta: 
        model = Office
        fields = '__all__'