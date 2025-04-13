from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contato/', views.contato, name='contato'),
    path('criar-conta/', views.criar_conta, name='criar_conta'),
    path('doacoes/', views.doacoes, name='doacoes'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('minha-conta/', views.minha_conta, name='minha_conta'),
]