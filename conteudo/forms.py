from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class Criarcontaform(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

class FormHome(forms.Form):
    email = forms.EmailField(label=False)