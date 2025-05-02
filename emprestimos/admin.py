import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Emprestimo, Livro 

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


    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="emprestimos.csv"'
        writer = csv.writer(response)
        writer.writerow(['usuario', 'livro', 'copia_id', 'data_emprestimo', 'data_devolucao', 'status'])
        for livro in queryset:
            writer.writerow([livro.usuario, livro.livro, livro.copia_id, livro.data_emprestimo, livro.data_devolucao, livro.status])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]      