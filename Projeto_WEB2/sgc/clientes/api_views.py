from django.db.models.deletion import ProtectedError
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet): # é uma classe "especial" que automaticamente cria 5 endpoints
    queryset = Cliente.objects.all() #  vai define quais dados estão disponiveis na API (no caso, todos os clientes)
    serializer_class = ClienteSerializer # define qual serializer vai ser usado para converter os dados

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object() # Busca o cliente a que deve ser excluido
        try:
            return super().destroy(request, *args, **kwargs) # Tenta excluir
        except ProtectedError: # caso tenha vendas associadas
            return Response(
                {'detail': 'Não é possível excluir um cliente com vendas associadas.'}, #Regra de negocio
                status=status.HTTP_409_CONFLICT, # Retorna o erro 409
            )
