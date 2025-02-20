from django.db import models
from core.escola.modelosteste import User, Turma

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=255)
    data_matricula = models.DateField()
    data_cancelamento = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.user.nome

    class Meta:
        db_table = 'aluno'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
