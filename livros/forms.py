from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class NomeSiteForm(forms.Form):
    nome_do_site = forms.CharField(
        label='Nome do Site', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do site'})
    )

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']