# empréstimos/forms.py

from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove o campo de senha que vem por padrão no UserChangeForm
        self.fields.pop('password', None)

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User