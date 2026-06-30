#Importação de modelos e lib
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Cliente
from vendas.models import Venda


class ClienteDeleteTests(TestCase):
    def setUp(self): # prepara o ambiente
        self.client = APIClient() # Cliente para fazer requisições
        self.user = User.objects.create_user(username='teste', password='123456')
        self.client.force_authenticate(user=self.user) # loga automatico
        
        # Teste de criação de usuário
        self.cliente = Cliente.objects.create(
            nome='Maria',
            cpf='123.456.789-00',
            email='maria@example.com',
            telefone='11999999999',
            endereco='Rua A, 10',
        )
        # Teste vendas
        self.venda = Venda.objects.create(
            cliente=self.cliente, # Vincula a venda a este cliente
            usuario=self.user,
            valor_total='100.00',
        )

    # Faz uma requisição DELETE para a API tentando excluir o cliente.
    def test_delete_cliente_with_sales_is_blocked(self):
        response = self.client.delete(f'/api/clientes/{self.cliente.pk}/')
        self.assertEqual(response.status_code, 409)
        self.assertTrue(Cliente.objects.filter(pk=self.cliente.pk).exists())
