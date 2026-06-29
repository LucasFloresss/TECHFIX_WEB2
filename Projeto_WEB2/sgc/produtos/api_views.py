from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

#Cria uma API CRUD completa para o modelo "produto" automaticamente
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
