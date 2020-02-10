from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': ' rounded-lg mb-4 bg-gray-400 ml-4 px-2 py-2'
            }
        )
    )
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
