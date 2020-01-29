from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'description',
            'Todo_date',
            'pub_date'
        ]
