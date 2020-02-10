from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': ' rounded-lg mb-6 bg-gray-400 ml-12 px-2 py-2'
            }
        )
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': ' rounded-lg mb-6 bg-gray-400 ml-2 px-2 pt-4 pb-6'
            }
        )
    )
    Todo_date = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'class': ' rounded-lg mb-6 bg-gray-400 ml-4 px-2 py-2'
            }
        )
    )
    pub_date = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'class': ' rounded-lg mb-6 bg-gray-400 ml-6 px-2 py-2'
            }
        )
    )

    class Meta:
        model = Todo
        fields = [
            'name',
            'description',
            'Todo_date',
            'pub_date'
        ]
