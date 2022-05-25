from django import forms
from .models import Department
from django.contrib.auth.models import User
class DropDownForm(forms.Form):
    menu = forms.ModelChoiceField(queryset=Department.objects.get_queryset())
    
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email','password')