from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .models import Gênero, Livro  # Importe o modelo Livro

def index(request):
    livros = Livro.objects.all().select_related('autor', 'gênero')  
    generos = Gênero.objects.filter(is_active=True).order_by('name')  
    
    context = {
        'livros': livros,
        'generos': generos
    }
    return render(request, 'index.html', context)

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

# Nova view de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Usuário ou senha inválidos.'})
    return JsonResponse({'success': False, 'error': 'Método não permitido.'})

# View de logout
def logout_view(request):
    logout(request)
    return redirect('home')