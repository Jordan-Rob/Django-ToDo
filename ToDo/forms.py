from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    name = forms.CharField(label_suffix='',
                           widget=forms.TextInput(
                               attrs={
                                   'class': ' rounded-lg mb-6 bg-gray-400 ml-12 px-2 py-2 focus:outline-none focus:bg-gray-100  focus:border-purple-600 '
                               }
                           )
                           )
    description = forms.CharField(label_suffix='',
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': ' rounded-lg mb-6 bg-gray-400 ml-2 px-2 pt-4 pb-6 focus:outline-none focus:bg-gray-100  focus:border-purple-600 '
                                      }
                                  )
                                  )
    Todo_date = forms.DateTimeField(label_suffix='',
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': ' rounded-lg mb-6 bg-gray-400 ml-4 px-2 py-2 focus:outline-none focus:bg-gray-100  focus:border-purple-600 '
                                        }
                                    )
                                    )
    pub_date = forms.DateTimeField(label_suffix='',
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': ' rounded-lg mb-6 bg-gray-400 ml-6 px-2 py-2 focus:outline-none focus:bg-gray-100  focus:border-purple-600 '
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


class TodoLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )
