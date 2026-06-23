from django.db.models.deletion import ProtectedError
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {'detail': 'Não é possível excluir um cliente com vendas associadas.'},
                status=status.HTTP_409_CONFLICT,
            )
