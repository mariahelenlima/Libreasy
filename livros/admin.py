import csv 
from django.http import HttpResponse
from django.contrib import admin
from .models import Editora, Gênero, Livro, Autor, Copia
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from livros.models import Copia

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at') #campos que aparecerão na gride admin
    #list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at') #campos que aparecerão na gride admin

    search_fields = ('name',) #procurar por nome
   # list_filter = ('is_active',) #filtrar por ativo ou inativo
    
@admin.register(Gênero)
class GêneroAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    #list_filter = ('is_active',)
    
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',) 
    #list_filter = ('is_active',) 
    
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'autor',
        'isbn',
        'serie',
        'edicao',
        'volume',
        'editora',
        'gênero',
        'capa_url',
        'description',
        'is_active',
    ]
    readonly_fields = ['created_at', 'updated_at']


    list_display = ('title', 'autor', 'editora', 'gênero', 'is_active', 'created_at', 'updated_at')

    search_fields = ('title', 'editora__name', 'gênero__name')
    list_filter = ('is_active', 'editora', 'gênero')
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="livros.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'editora', 'gênero', 'ativo', 'descrição', 'criado em', 'atualizado em'])

        for livro in queryset:
            writer.writerow([livro.title, livro.editora.name, livro.gênero.name, livro.is_active, livro.description, livro.created_at, livro.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]  


@admin.register(Copia)
class CopiasAdmin(admin.ModelAdmin):
    list_select_related = ['livro', 'livro__autor', 'livro__editora', 'livro__gênero']
    fields = [
        'livro',  # Só o campo 'livro' é necessário aqui
        'tombamento',
       # 'is_active',
        'status',
        # 'title',
        # 'autor',
        # 'isbn',
        # 'serie',
        # 'edicao',
        # 'volume',
        # 'editora',
        # 'gênero',
        # 'capa_url',
        # 'description',
        
    ]
    list_display = ('tombamento', 'livro', 'get_autor', 'get_isbn', 'status', 'created_at')
    #list_display = ('tombamento', 'livro', 'get_isbn', 'get_autor', 'created_at', 'is_active')

    search_fields = ('livro__title',)

    def get_isbn(self, obj):
        return obj.livro.isbn  # Obtém o ISBN do livro relacionado
    get_isbn.short_description = 'ISBN'

    def get_autor(self, obj):
        return obj.livro.autor  # Obtém o autor do livro relacionado
    get_autor.short_description = 'Autor'

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="copias.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'autor','editora', 'gênero', 'ativo', 'descrição', 'criado em', 'atualizado em'])

        for copia in queryset:
            writer.writerow([copia.livro.title, copia.livro.autor.name if copia.livro.autor else '', 
                             copia.livro.editora.name if copia.livro.editora.name else '', 
                             copia.livro.gênero.name if copia.livro.gênero.name else '', 
                             copia.livro.is_active, 
                             copia.livro.description if hasattr(copia.livro, 'description') else '', 
                             copia.livro.created_at, 
                             copia.livro.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]  


###############################################
# Desregistrar o modelo Group do admin
admin.site.unregister(Group)

# Alterar o nome do modelo "Group" para "Permissões"
Group._meta.verbose_name = _("Permissões")
Group._meta.verbose_name_plural = _("Permissões")

# Registrar novamente o modelo no admin
admin.site.register(Group)
###############################################



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from django import forms

# class CustomUserChangeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Remove o campo 'password' do formulário
#         self.fields.pop('password', None)

# class CustomUserAdmin(BaseUserAdmin):
#     form = CustomUserChangeForm
#     fieldsets = (
#         (None, {'fields': ('username',)}),
#         ('Informações pessoais', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
#     )

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse

class CustomUserAdmin(BaseUserAdmin):
    def password_change_link(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return format_html('<a href="{}">Clique aqui para alterar a senha</a>', url)
    password_change_link.short_description = "Senha"

    fieldsets = (
        (None, {'fields': ('username', 'password_change_link')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('password_change_link',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
