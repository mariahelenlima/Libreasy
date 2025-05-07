from django.db import models
from django.contrib.auth.models import User
from livros.models import Copia
from django.utils import timezone

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('EMPRESTADO', 'Emprestado'),
        ('EM_ATRASO', 'Em Atraso'), # = emprestado
        ('DEVOLVIDO', 'Devolvido'), # = disponivel 
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    copia = models.ForeignKey(Copia, on_delete=models.PROTECT, verbose_name='Tombamento/Livro/ISBN:')
    data_emprestimo = models.DateField(default=timezone.now, verbose_name='Data de Empréstimo')
    data_devolucao = models.DateField(verbose_name='Prazo de Devolução')
    data_devolucao_real = models.DateField(null=True, blank=True, verbose_name='Data de Devolução')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EMPRESTADO', verbose_name='Situação')

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f"{self.usuario.username} - {self.copia.livro.title} ({self.copia.tombamento})"


    def atualizar_status(self):
        hoje = timezone.now().date()
        if self.status not in ['DEVOLVIDO']:
            if hoje > self.data_devolucao:
                self.status = 'EM_ATRASO'
            else:
                self.status = 'EMPRESTADO'

    def save(self, *args, **kwargs):
        self.atualizar_status()
        super().save(*args, **kwargs)
        # Atualiza o status da cópia conforme o status do empréstimo
        if self.status == 'DEVOLVIDO':
            self.copia.status = 'DISPONIVEL'
        else:
            self.copia.status = 'EMPRESTADO'
        self.copia.save()
