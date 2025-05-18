import csv 
from django.http import HttpResponse
from django.contrib import admin
from .models import Editora, Gênero, Livro, Autor, Copia
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from livros.models import Copia
from typing import Set
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at') #campos que aparecerão na gride admin
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
        'status',
    ]
    list_display = ('tombamento', 'livro', 'get_autor', 'status', 'created_at')
    search_fields = ('livro__title',)

    def get_isbn(self, obj):
        return obj.livro.isbn  #Obtém o ISBN do livro relacionado
    get_isbn.short_description = 'ISBN'

    def get_autor(self, obj):
        return obj.livro.autor  #Obtém o autor do livro relacionado
    get_autor.short_description = 'Autor'

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="copias.csv"'
        writer = csv.writer(response)
        writer.writerow(['número de tombamento', 'título', 'autor','editora', 'gênero', 'criado em', 'atualizado em'])

        for copia in queryset:
            writer.writerow([copia.tombamento, copia.livro.title, 
                             copia.livro.autor.name if copia.livro.autor else '', 
                             copia.livro.editora.name if copia.livro.editora.name else '', 
                             copia.livro.gênero.name if copia.livro.gênero.name else '', 
                             #copia.livro.description if hasattr(copia.livro, 'description') else '', 
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

USUARIOS_PROTEGIDOS = ['Libreasy', 'Desenvolvedor']
USUARIOS_ADMINISTRADORES = ['Administrador']

#@admin.register(User)
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

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        is_superuser = request.user.is_superuser
        #in_allowed_group = request.user.groups.filter(name='Administrador').exists()
        #is_admin_user = request.user.username in USUARIOS_ADMINISTRADORES

        # Remove o campo 'is_superuser' para membros do grupo "Administrador"
        #if not is_superuser and in_allowed_group:
        #if not is_superuser and is_admin_user:
        if not is_superuser:
            updated_fieldsets = []
            for name, data in fieldsets:
                fields = list(data.get('fields', []))
                if 'is_superuser' in fields:
                    fields.remove('is_superuser')
                updated_fieldsets.append((name, {'fields': fields}))
            return updated_fieldsets

        return fieldsets
    #ver dps o que faz

    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        #if not request.user.is_superuser and request.user.groups.filter(name='Administrador').exists():
        if request.user.username in USUARIOS_ADMINISTRADORES:
            readonly.append('is_superuser')
        return readonly

    def has_change_permission(self, request, obj=None):
        if obj and obj.username in USUARIOS_PROTEGIDOS:
            return False  # Ninguém pode editar esses usuários
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.username in USUARIOS_PROTEGIDOS:
            return False  # Ninguém pode excluir esses usuários
        return super().has_delete_permission(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        #in_allowed_group = request.user.groups.filter(name='Administrador').exists()
        #is_admin_user = request.user.groups.filter(name='Administrador').exists()
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
        #if not is_superuser and not in_allowed_group:
        #if not is_superuser and not  is_admin_user:
            disabled_fields |= {
                #'username',
                'is_superuser',
                'user_permissions', #remover acesso para user mudar próprias permissoes   conceder permissões somente usando grupos
            }

       
        #if not is_superuser: #and not in_allowed_group and obj is not None and obj == request.user:
             # Impede que o próprio usuário (não superuser e não admin) altere seu nível de acesso
        #if not is_superuser and not in_allowed_group and obj is not None and obj == request.user:
        #if not is_superuser and not is_admin_user and obj is not None and obj == request.user:
        if not is_superuser  and obj is not None and obj == request.user:  
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                #'groups',
                'user_permissions',
            }
#ver dps 

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

#admin.site.disable_action('delete_selected') #desabilitar ações de remossão em massa