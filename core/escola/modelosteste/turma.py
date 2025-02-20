from django.db import models
from core.escola.modelosteste import User
from core.escola.modelosteste import Escola

class Turma(models.Model):
    nome = models.CharField(max_length=255)
    turno = models.CharField(max_length=255)
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    disciplina = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'turma'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'