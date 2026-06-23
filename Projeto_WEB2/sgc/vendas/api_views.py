from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import Venda, ItemVenda
from .serializers import VendaSerializer, VendaCreateSerializer
from clientes.models import Cliente
from produtos.models import Produto

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    http_method_names = ['get', 'post', 'delete']

    def create(self, request):
        serializer = VendaCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        if not data['itens']:
            return Response({'erro': 'Venda deve ter ao menos um item.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cliente = Cliente.objects.get(pk=data['cliente'])
        except Cliente.DoesNotExist:
            return Response({'erro': 'Cliente não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            venda = Venda.objects.create(cliente=cliente, usuario=request.user, valor_total=0)
            total = 0

            for item_data in data['itens']:
                try:
                    produto = Produto.objects.get(pk=item_data['produto'])
                except Produto.DoesNotExist:
                    raise Exception(f'Produto {item_data["produto"]} não encontrado.')

                if produto.quantidade_estoque < item_data['quantidade']:
                    raise Exception(f'Estoque insuficiente para {produto.nome}.')

                produto.quantidade_estoque -= item_data['quantidade']
                produto.save()

                ItemVenda.objects.create(
                    venda=venda,
                    produto=produto,
                    quantidade=item_data['quantidade'],
                    preco_unitario=produto.preco,
                )
                total += produto.preco * item_data['quantidade']

            venda.valor_total = total
            venda.save()

        return Response(VendaSerializer(venda).data, status=status.HTTP_201_CREATED)
