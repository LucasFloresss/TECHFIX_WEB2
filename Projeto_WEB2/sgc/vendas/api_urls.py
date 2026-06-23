from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import VendaViewSet

router = DefaultRouter()
router.register('vendas', VendaViewSet)

urlpatterns = [path('', include(router.urls))]
