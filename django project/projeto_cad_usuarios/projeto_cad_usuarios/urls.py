from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome referência
    #usuarios.com = endereço local
    path('',views.home, name='home'),

    #usuarios.com/usuarios = endereço local/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
