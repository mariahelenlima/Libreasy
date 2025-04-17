from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'copia_id', 'data_emprestimo', 'data_devolucao', 'status')
    list_filter = ('status', 'data_emprestimo')
    search_fields = ('usuario__username', 'livro__title', 'copia_id')
    date_hierarchy = 'data_emprestimo'
    actions = ['marcar_como_devolvido']

    def marcar_como_devolvido(self, request, queryset):
        updated = queryset.update(status='DEVOLVIDO', data_devolucao_real=timezone.now().date())
        self.message_user(request, f"{updated} empréstimo(s) marcado(s) como devolvido(s).")
    marcar_como_devolvido.short_description = "Marcar como devolvido"