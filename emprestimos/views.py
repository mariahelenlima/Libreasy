from emprestimos.models import Emprestimo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import EditUserForm, CustomPasswordChangeForm


@login_required
def minha_conta(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user).order_by('-data_emprestimo')
    
    # Atualiza status dos empréstimos
    for emprestimo in emprestimos:
        emprestimo.atualizar_status()
    
    user_form = EditUserForm(instance=request.user)
    password_form = CustomPasswordChangeForm(user=request.user)
    
    if request.method == 'POST':
        if 'save_user' in request.POST:
            user_form = EditUserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Dados atualizados com sucesso!')
                return redirect('minha_conta')
            else:
                messages.error(request, 'Erro no formulário. Verifique os dados.')
        
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            
            if password_form.is_valid():
                password_form.save()
                messages.success(request, 'Senha alterada com sucesso!')
                return redirect('minha_conta')
            else:
                # Captura todos os erros do formulário
                for field, error_list in password_form.errors.items():
                    for error in error_list:
                        messages.error(request, error)

    
    context = {
        'emprestimos': emprestimos,
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'minha-conta.html', context)

