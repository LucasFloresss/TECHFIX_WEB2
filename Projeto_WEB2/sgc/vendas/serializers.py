from rest_framework import serializers
from .models import Venda, ItemVenda
from clientes.serializers import ClienteSerializer
from produtos.serializers import ProdutoSerializer

class ItemVendaSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = ItemVenda
        fields = ['id', 'produto', 'produto_nome', 'quantidade', 'preco_unitario', 'subtotal']

    def get_subtotal(self, obj):
        return obj.subtotal()

class ItemVendaCreateSerializer(serializers.Serializer):
    produto = serializers.IntegerField()
    quantidade = serializers.IntegerField(min_value=1)

class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True, read_only=True)
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    usuario_nome = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Venda
        fields = ['id', 'data', 'cliente', 'cliente_nome', 'usuario', 'usuario_nome', 'valor_total', 'itens']
        read_only_fields = ['usuario', 'valor_total', 'data']

class VendaCreateSerializer(serializers.Serializer):
    cliente = serializers.IntegerField()
    itens = ItemVendaCreateSerializer(many=True)
