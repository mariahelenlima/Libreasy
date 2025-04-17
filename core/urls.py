from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Painel de administração do Django
    path('', include('livros.urls')),  # Inclui as URLs do app 'livros'
    path('emprestimos/', include('emprestimos.urls')),
]