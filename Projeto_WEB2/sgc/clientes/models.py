from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
