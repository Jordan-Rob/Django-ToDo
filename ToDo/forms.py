from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField()
    Todo_date = forms.DateTimeField()
    pub_date = forms.DateTimeField()

    class Meta:
        model = Todo
        fields = [
            'name',
            'description',
            'Todo_date',
            'pub_date'
        ]
