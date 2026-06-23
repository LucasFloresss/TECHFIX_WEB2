from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ClienteViewSet

router = DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [path('', include(router.urls))]
