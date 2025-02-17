from django.contrib import admin
import core.escola.models as models


admin.site.register(models.Escola)
admin.site.register(models.Turma)
admin.site.register(models.User)
admin.site.register(models.Professor)
admin.site.register(models.Aluno)


# Register your models here.
