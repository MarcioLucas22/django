from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    estoque = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
