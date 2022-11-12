from django import forms
from django.contrib.auth.models import Group, User
from apps.profiles.models import*
from allauth.account.adapter import get_adapter
from django.contrib.auth import authenticate

class CustomerForm(forms.ModelForm):
    class Meta: 
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
       super(CustomerForm, self).__init__(*args, **kwargs)
       self.fields['user'].required = False

class UserForm(forms.ModelForm):
    new_password=forms.CharField(widget=forms.PasswordInput())
    repeat_password=forms.CharField(widget=forms.PasswordInput())
    rol=forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta:
        model = User
        fields=[
            'username',
            'email',
            'first_name',
            'last_name',
            'repeat_password',
            'new_password',
            'rol',
            'is_active'

        ]
    
    def _init_(self, *args, **kwargs):
       super(UserForm, self)._init_(*args, **kwargs)
       self.fields['first_name'].required=True
       self.fields['last_name'].required=True
    
    def clean_new_password(self):
        new_password=self.cleaned_data.get('new_password')
        repeat_password=self.cleaned_data.get('repeat_password')
        if new_password!=repeat_password:
            raise forms.ValidationError(('Las contraseñas deben ser iguales'), code='invalid')
        else:
            #get_adapter().clean_password genera las validaciones para que la contraseña tenga los protocolos de una contraseña segura
            validation=get_adapter().clean_password(new_password)
        return self.cleaned_data

class UserUpdateForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = [
        
            'first_name',
            'last_name',
            'is_active'
        ]



   