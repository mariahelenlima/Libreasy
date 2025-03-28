from django import forms

class NomeSiteForm(forms.Form):
    nome_do_site = forms.CharField(
        label='Nome do Site', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do site'})
    )