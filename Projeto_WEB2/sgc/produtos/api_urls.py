from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ProdutoViewSet

# Gera todas as rotas REST para o ProdutoViewSet automaticamente.
router = DefaultRouter()
router.register('produtos', ProdutoViewSet)

urlpatterns = [path('', include(router.urls))]
