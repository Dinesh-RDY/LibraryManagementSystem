from django import forms
from .models import Department
class DropDownForm(forms.Form):
    menu = forms.ModelChoiceField(queryset=Department.objects.get_queryset())
    