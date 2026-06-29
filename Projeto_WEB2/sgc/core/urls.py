from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def login_view(request):
    return render(request, 'login.html')

urlpatterns = [
    path('', RedirectView.as_view(url='/clientes/', permanent=False)),
    path('admin/', admin.site.urls), # Painel administrativo do Django para gerenciar dados (clientes, vendas, usuarios e etc.)
    path('login/', login_view, name='login'), # Página de login

    # API de autenticação
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # API REST
    path('api/', include('clientes.api_urls')),
    path('api/', include('produtos.api_urls')),
    path('api/', include('vendas.api_urls')),
    path('api/', include('relatorios.api_urls')),

    # Interface na web bombastica
    path('', include('clientes.urls')),
    path('', include('produtos.urls')),
    path('', include('vendas.urls')),
    path('', include('relatorios.urls')),
]
