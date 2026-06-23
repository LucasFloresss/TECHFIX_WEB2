from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista, name='produtos'),
    path('produtos/novo/', views.form, name='produto_novo'),
    path('produtos/<int:pk>/editar/', views.form, name='produto_editar'),
]
