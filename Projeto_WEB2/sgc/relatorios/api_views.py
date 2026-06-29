from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from vendas.models import Venda
import datetime

# isso tudo efine 3 endpoints de API para consultar dados de vendas com diferentes filtros

class RelatorioPeriodo(APIView): # vendas em um período específico
    def get(self, request):
        data_inicio = request.query_params.get('inicio')
        data_fim = request.query_params.get('fim')

        vendas = Venda.objects.all()
        if data_inicio:
            vendas = vendas.filter(data__date__gte=data_inicio)
        if data_fim:
            vendas = vendas.filter(data__date__lte=data_fim)

        total = vendas.aggregate(total=Sum('valor_total'))['total'] or 0
        quantidade = vendas.count()

        return Response({
            'total': total,
            'quantidade': quantidade,
            'vendas': [
                {
                    'id': v.id,
                    'data': v.data.strftime('%d/%m/%Y %H:%M'),
                    'cliente': v.cliente.nome,
                    'usuario': v.usuario.username,
                    'valor_total': str(v.valor_total),
                }
                for v in vendas
            ]
        })

class RelatorioCliente(APIView): # Vendas de um cliente específico
    def get(self, request):
        cliente_id = request.query_params.get('cliente_id')
        if not cliente_id:
            return Response({'erro': 'Informe o cliente_id.'}, status=400)

        vendas = Venda.objects.filter(cliente_id=cliente_id)
        total = vendas.aggregate(total=Sum('valor_total'))['total'] or 0

        return Response({
            'total': total,
            'quantidade': vendas.count(),
            'vendas': [
                {
                    'id': v.id,
                    'data': v.data.strftime('%d/%m/%Y %H:%M'),
                    'valor_total': str(v.valor_total),
                }
                for v in vendas
            ]
        })

class RelatorioAnual(APIView): # Vendas por mês do ano
    def get(self, request):
        ano = request.query_params.get('ano', datetime.date.today().year)

        vendas = (
            Venda.objects
            .filter(data__year=ano)
            .annotate(mes=TruncMonth('data'))
            .values('mes')
            .annotate(total=Sum('valor_total'), quantidade=Count('id'))
            .order_by('mes')
        )

        meses = {i: {'mes': i, 'total': 0, 'quantidade': 0} for i in range(1, 13)}
        for v in vendas:
            m = v['mes'].month
            meses[m] = {'mes': m, 'total': float(v['total']), 'quantidade': v['quantidade']}

        return Response({'ano': ano, 'meses': list(meses.values())})
