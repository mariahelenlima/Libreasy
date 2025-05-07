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
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT,
    related_name='livros', verbose_name='Autor')

    isbn = models.IntegerField(unique=True, verbose_name='ISBN')
    serie = models.CharField(max_length=50, blank=True, default='', verbose_name='Série')
    edicao = models.IntegerField(default=1, verbose_name='Edição')
    volume = models.IntegerField(default=1, verbose_name='Volume')

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
        return f"{self.title} (ISBN: {self.isbn}, Autor: {self.autor})"
    
    # funções para contar a quantidade de cópias
    @property
    def copias_disponiveis(self):
        return self.copias.filter(status='DISPONIVEL').count()
    
    @property
    def copias_emprestadas(self):
        return self.copias.filter(status='EMPRESTADO').count()
    
    @property
    def total_copias(self):
        return self.copias.count()

# Modelo Cópias
class Copia(models.Model):
    tombamento = models.CharField(max_length=50, unique=True, verbose_name='Tombamento')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='copias', verbose_name='Livro')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    # tentativa de adicionar o campo de status
    STATUS_CHOICES = [
        ('EMPRESTADO', 'Emprestado'),
        ('DISPONIVEL', 'Disponível'),
    ]
        
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL', verbose_name='Situação')
    ### fim
    class Meta:
        ordering = ['tombamento']
        verbose_name = 'Copia'

    def __str__(self):
        return f"{self.tombamento} (Título: {self.livro.title}, ISBN: {self.livro.isbn})"