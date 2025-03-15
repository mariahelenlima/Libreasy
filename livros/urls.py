from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('contato/', views.contato, name='contato'),
        path('criar-conta/', views.criar_conta, name='criar_conta'),
        path('doacoes/', views.doacoes, name='doacoes'),  # URL corrigida
    ]