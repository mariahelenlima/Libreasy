# Generated by Django 5.0 on 2025-03-26 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_livro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa_url',
            field=models.URLField(blank=True, help_text='URL completa da imagem (ex: https://exemplo.com/imagem.jpg)', max_length=500, null=True),
        ),
    ]
