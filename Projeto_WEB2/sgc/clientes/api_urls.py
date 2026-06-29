from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ClienteViewSet

router = DefaultRouter() # roteador automático do DRF que gera todas as URLs REST
router.register('clientes', ClienteViewSet) # cria automaticamente todas as rotas CRUD
urlpatterns = [path('', include(router.urls))] # inclui todas as URL geradas pelo router no projeto
