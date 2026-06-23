from django.urls import path
from .api_views import RelatorioPeriodo, RelatorioCliente, RelatorioAnual

urlpatterns = [
    path('relatorios/periodo/', RelatorioPeriodo.as_view(), name='relatorio_periodo'),
    path('relatorios/cliente/', RelatorioCliente.as_view(), name='relatorio_cliente'),
    path('relatorios/anual/', RelatorioAnual.as_view(), name='relatorio_anual'),
]
