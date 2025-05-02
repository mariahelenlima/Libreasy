import csv 
from django.http import HttpResponse
from django.contrib import admin
from .models import Editora, Gênero, Livro, Autor

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at') #campos que aparecerão na gride admin
    search_fields = ('name',) #procurar por nome
    list_filter = ('is_active',) #filtrar por ativo ou inativo
    
@admin.register(Gênero)
class GêneroAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',) 
    list_filter = ('is_active',) 
    
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('title', 'editora', 'gênero', 'capa_url', 'price', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'editora__name', 'gênero__name')
    list_filter = ('is_active', 'editora', 'gênero')
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="livros.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'editora', 'gênero', 'preço', 'ativo', 'descrição', 'criado em', 'atualizado em'])
        for livro in queryset:
            writer.writerow([livro.title, livro.editora.name, livro.gênero.name, livro.price, livro.is_active, livro.description, livro.created_at, livro.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]  

