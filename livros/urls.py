from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contato/', views.contato, name='contato'),
    path('criar-conta/', views.criar_conta, name='criar_conta'),
    path('doacoes/', views.doacoes, name='doacoes'),
#   path('login-view/', views.login_view, name='login_view'),  # Nova URL de login
    path('logout/', views.logout_view, name='logout'),  # Nova URL de logout
    path('login/', views.login, name='login'),  #  URL de login
   # path('login/', include('django.contrib.auth.urls'), views.login, name='login'),
    path('minha-conta/', views.minha_conta, name='minha_conta'),  # URL Minha-Conta
]