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

#class ChangePasswordForm(PasswordChangeForm):
#    class Meta:
#        model = User

from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise ValidationError(_("Senha atual incorreta"))
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Novas senhas não coincidem"))
        
        # Validação de tamanho mínimo (8 caracteres por exemplo)
        if len(password1) < 8:
            raise ValidationError(_("Erro: Nova senha deve possuir no mínimo 8 carácteres."))
            
        return password2