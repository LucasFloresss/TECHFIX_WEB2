from django.db import models

class Produto(models.Model): #modelo da tabela
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=5)

    def __str__(self):
        return self.nome #define como o produto é exibido no admin e em select

    class Meta: 
        ordering = ['nome'] #ordena em ordem alfabetica
