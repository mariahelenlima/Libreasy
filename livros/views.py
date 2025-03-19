from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Livro  # Importe o modelo Livro


def index(request):
    livros = Livro.objects.all()  # Busca todos os livros do banco de dados
    return render(request, 'index.html', {'livros': livros})  # Envia os livros para o template

def contato(request):
    return render(request, 'contato.html')

def criar_conta(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')
    else:
        form = UserCreationForm()
    
    return render(request, 'criar-conta.html', {'form': form})

def doacoes(request):
    return render(request, 'doacoes.html')