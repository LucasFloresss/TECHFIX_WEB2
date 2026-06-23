from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ProdutoViewSet

router = DefaultRouter()
router.register('produtos', ProdutoViewSet)

urlpatterns = [path('', include(router.urls))]
