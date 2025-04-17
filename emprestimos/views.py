from emprestimos.models import Emprestimo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def minha_conta(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user).order_by('-data_emprestimo')
    
    # Atualiza status dos empréstimos
    for emprestimo in emprestimos:
        emprestimo.atualizar_status()
    
    context = {
        'emprestimos': emprestimos,
    }
    return render(request, 'minha-conta.html', context)