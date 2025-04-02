from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .models import Gênero, Livro  # Importe o modelo Livro
from django.contrib.auth.decorators import login_required
# formulario de login importado de livros/forms.py
from .forms import CreateUserForm

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

# Nova view de login
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(user)
            return redirect('minha-conta')
        else:
            messages.info(request, 'Usuario ou senha incorretos')
            return JsonResponse({'success': True})
        #else:
            #return JsonResponse({'success': False, 'error': 'Usuário ou senha inválidos.'})
            #return JsonResponse({'success': False, 'error': 'Método não permitido.'})
        
    context = {}
    return render(request, 'login.html', context)

# View de logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Página Login
#def login(request):
#    return render(request, 'login.html')

@login_required
def minha_conta(request):
    return render(request, 'minha-conta.html')