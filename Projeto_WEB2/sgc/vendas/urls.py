from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.lista, name='vendas'),
    path('vendas/nova/', views.nova, name='venda_nova'),
    path('vendas/<int:pk>/', views.detalhe, name='venda_detalhe'),
]
