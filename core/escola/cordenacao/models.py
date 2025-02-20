from django.db import models

# Create your models here.
class teste(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome