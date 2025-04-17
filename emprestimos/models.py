from django.db import models
from django.contrib.auth.models import User
from livros.models import Livro
from django.utils import timezone

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('EMPRESTADO', 'Emprestado'),
        ('EM_ATRASO', 'Em atraso'),
        ('DEVOLVIDO', 'Devolvido'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, verbose_name='Livro')
    copia_id = models.CharField(max_length=50, verbose_name='ID da Cópia', help_text='Identificador único da cópia física')
    data_emprestimo = models.DateField(default=timezone.now, verbose_name='Data de Empréstimo')
    data_devolucao = models.DateField(verbose_name='Data de Devolução')
    data_devolucao_real = models.DateField(null=True, blank=True, verbose_name='Data Real de Devolução')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EMPRESTADO', verbose_name='Status')

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f"{self.usuario.username} - {self.livro.title}"

    def atualizar_status(self):
        hoje = timezone.now().date()
        if self.status != 'DEVOLVIDO':
            if hoje > self.data_devolucao:
                self.status = 'EM_ATRASO'
            else:
                self.status = 'EMPRESTADO'
            self.save()
        return self.status