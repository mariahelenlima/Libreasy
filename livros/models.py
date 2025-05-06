from django.db import models

#Modelo Autor
class Autor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Autor'

    def __str__(self):
        return self.name

# Modelo Editora
class Editora(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Editora'

    def __str__(self):
        return self.name

# Modelo Gênero
class Gênero(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Gênero'

    def __str__(self):
        return self.name

# Modelo Livro
class Livro(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT,
        related_name='livros', verbose_name='Editora')
    gênero = models.ForeignKey(Gênero, on_delete=models.PROTECT,
        related_name='livros', verbose_name='Gênero')
    
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT,
    related_name='livros', verbose_name='Autor')

    capa_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="URL completa da imagem (ex: https://exemplo.com/imagem.jpg)"
    )
    
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['title']
        verbose_name = 'Livro'

    def __str__(self):
        return self.title

