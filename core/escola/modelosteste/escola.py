from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'escola'
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'