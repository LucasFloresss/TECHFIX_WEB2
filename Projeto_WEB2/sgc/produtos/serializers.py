from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    estoque_baixo = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = '__all__'

    def get_estoque_baixo(self, obj):
        return obj.quantidade_estoque <= obj.estoque_minimo

    def validate_preco(self, value):
        if value < 0:
            raise serializers.ValidationError('Preço não pode ser negativo.')
        return value
