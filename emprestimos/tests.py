from django.test import TestCase

# Create your tests here.

import csv #biblioteca nativa
from django.http import HttpResponse
from django.contrib import admin
# Register your models here.
#from .models import Brand, Category, Product
from .models import Editora, Gênero, Livro, Autor

# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at') #campos que vão aparecer na gride admin
#     search_fields = ('name',) #procurar, procurar por nome
#     list_filter = ('is_active',) #filtros, filtrar por ativo ou inativo
@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at') #campos que vão aparecer na gride admin
    search_fields = ('name',) #procurar, procurar por nome
    list_filter = ('is_active',) #filtros, filtrar por ativo ou inativo
    
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
#     search_fields = ('name',)
#     list_filter = ('is_active',)
@admin.register(Gênero)
class GêneroAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    
    
#autor
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at') #campos que vão aparecer na gride admin
    search_fields = ('name',) #procurar, procurar por nome
    list_filter = ('is_active',) #filtros, filtrar por ativo ou inativo
    
    #criar arquivo csv com tabela dos produtos
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'brand', 'category', 'price',
#                     'is_active', 'created_at', 'updated_at')
#     search_fields = ('title', 'brand__name', 'category__name')
#     list_filter = ('is_active', 'brand', 'category')
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('title', 'editora', 'gênero', 'capa_url', 'price',
                    'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'editora__name', 'gênero__name')
    list_filter = ('is_active', 'editora', 'gênero')
    
    # def export_to_csv(self, request, queryset):
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename="livros.csv"'
    #     writer = csv.writer(response)
    #     writer.writerow(['título', 'marca', 'categoria', 'preço',
    #                      'ativo', 'descrição', 'criado em', 'atualizado em'])
    #     for product in queryset:
    #         writer.writerow([product.title, product.brand.name, product.category.name,
    #                          product.price, product.is_active, product.description,
    #                          product.created_at, product.updated_at])
    #     return response

    # export_to_csv.short_description = 'Exportar para CSV'
    # actions = [export_to_csv]
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="livros.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'editora', 'gênero', 'preço',
                         'ativo', 'descrição', 'criado em', 'atualizado em'])
        for livro in queryset:
            writer.writerow([livro.title, livro.editora.name, livro.gênero.name,
                             livro.price, livro.is_active, livro.description,
                             livro.created_at, livro.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]
    
    
    
