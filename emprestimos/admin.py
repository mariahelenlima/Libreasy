import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils import timezone
from .models import Emprestimo
from livros.models import Copia

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'get_livro', 'get_tombamento', 'data_emprestimo', 'data_devolucao', 'status')
    list_filter = ('status', 'data_emprestimo')
    search_fields = ('usuario__username', 'livro__title', 'copia__tombamento')
    date_hierarchy = 'data_emprestimo'
    actions = ['marcar_como_devolvido', 'export_to_csv']

    def get_tombamento(self, obj):
        return obj.copia.tombamento
    get_tombamento.short_description = 'Tombamento'

    def get_livro(self, obj):
        return obj.copia.livro.title
    get_livro.short_description = 'Livro'


    def marcar_como_devolvido(self, request, queryset):
        for emprestimo in queryset:
            emprestimo.status = 'DEVOLVIDO'
            emprestimo.data_devolucao_real = timezone.now().date()
            emprestimo.save()  # Isso vai atualizar também o status da cópia via método save()

        self.message_user(request, f"{queryset.count()} empréstimo(s) marcado(s) como devolvido(s).")
    marcar_como_devolvido.short_description = "Marcar como devolvido"

    # def export_to_csv(self, request, queryset):
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename="emprestimos.csv"'
    #     writer = csv.writer(response)
    #     # writer.writerow(['Usuário', 'Livro', 'Tombamento', 'Data Empréstimo', 
    #     #                  'Data Devolução', 'Status'])
    #     writer.writerow(['Cópia', 'Título do Livro', 'Usuário', 
    #                      'Data Empréstimo', 'Data Devolução'])
    #     for emprestimo in queryset:
    #         writer.writerow([
    #             emprestimo.usuario.username,
    #             emprestimo.livro.title,
    #             emprestimo.copia.tombamento,
    #             emprestimo.data_emprestimo,
    #             emprestimo.data_devolucao,
    #             emprestimo.status
    #         ])
    #     return response
    
    def export_to_csv(self, request, queryset):
       response = HttpResponse(content_type='text/csv')
       response['Content-Disposition'] = 'attachment; filename="emprestimos.csv"'
       writer = csv.writer(response)
       writer.writerow(['Leitor', 'Título do Livro', 'Tombamento', 
                    'Data Empréstimo', 'Data Devolução', 'Status'])
    
       for emprestimo in queryset:
          writer.writerow([
              emprestimo.usuario.username,
              emprestimo.copia.livro.title if emprestimo.copia and emprestimo.copia.livro else 'N/A',
              emprestimo.copia.tombamento if emprestimo.copia else 'N/A',
              emprestimo.data_emprestimo,
              emprestimo.data_devolucao,
              emprestimo.status
        ])
       return response

    export_to_csv.short_description = 'Exportar para CSV'
