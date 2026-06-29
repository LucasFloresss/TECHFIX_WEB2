from django.urls import path
from . import views

# Mapeia as URLS
urlpatterns = [
    path('clientes/', views.lista, name='clientes'), # Quando acessar "clientes" ele chama a lista
    path('clientes/novo/', views.form, name='cliente_novo'), # Chama o formulario
    path('clientes/<int:pk>/editar/', views.form, name='cliente_editar'), # Chama formulario para editar
]
