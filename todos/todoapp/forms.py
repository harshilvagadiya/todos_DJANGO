from django import forms
from .models import myTodo

class toDoForms(forms.ModelForm):
    class Meta:
        model = myTodo
        fields = ('task',)