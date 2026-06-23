from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista, name='clientes'),
    path('clientes/novo/', views.form, name='cliente_novo'),
    path('clientes/<int:pk>/editar/', views.form, name='cliente_editar'),
]
