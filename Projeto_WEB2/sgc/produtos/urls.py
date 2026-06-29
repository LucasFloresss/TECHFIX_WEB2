from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista, name='produtos'), #listar
    path('produtos/novo/', views.form, name='produto_novo'), #cria
    path('produtos/<int:pk>/editar/', views.form, name='produto_editar'), #edita kkk
]
