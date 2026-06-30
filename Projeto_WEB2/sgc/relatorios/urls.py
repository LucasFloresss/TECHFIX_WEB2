from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/', views.index, name='relatorios'), # define uma única rota para a página de relatórios do sistema.
]
