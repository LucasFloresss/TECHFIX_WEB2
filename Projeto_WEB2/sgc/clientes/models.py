from django.db import models

# Define o modelo "cliente", que vai se tornar uma tabela no banco de dados com os campos especificados.
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=300)

    def __str__(self): # Define que o objeto será texto
        return self.nome
    class Meta:
        ordering = ['nome'] # sempre que buscar clientes, eles virão ordenados alfabeticamente usando o nome
