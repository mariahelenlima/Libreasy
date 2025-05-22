from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse
from .models import Gênero, Livro
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from emprestimos.models import Emprestimo
from django.contrib.auth.decorators import login_required

def index(request):
    #livros = Livro.objects.all() \
    livros = Livro.objects.filter(is_active=True) \
                .select_related('autor', 'gênero') \
                 .prefetch_related('copias')

    #generos = Gênero.objects.filter(is_active=True).order_by('name')  
    generos = Gênero.objects.all().order_by('name')  # Remove o filter(is_active=True)
    
    context = {
        'livros': livros,
        'generos': generos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def criar_conta(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')
    else:
        form = CreateUserForm()
    
    return render(request, 'criar-conta.html', {'form': form})

def doacoes(request):
    return render(request, 'doacoes.html')

def desenvolvedores(request):
    return render(request, 'desenvolvedores.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('minha_conta')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
    
    return render(request, 'login.html')

@require_POST
def logout_view(request):
    logout(request)
    return redirect('home')

