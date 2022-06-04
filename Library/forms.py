from django import forms
from .models import Department
from django.contrib.auth.models import User


class DropDownForm(forms.Form):
    queryset = Department.objects.get_queryset()
    menu = forms.ModelChoiceField(queryset=queryset)


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
