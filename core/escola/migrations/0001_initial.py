# Generated by Django 5.1.6 on 2025-02-17 12:04

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('telefone', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=255)),
                ('ativa', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Escola',
                'verbose_name_plural': 'Escolas',
                'db_table': 'escola',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('telefone', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('turno', models.CharField(max_length=255)),
                ('disciplina', models.CharField(max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('ativa', models.BooleanField(default=True)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.escola')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.user')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'db_table': 'turma',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacao', models.CharField(max_length=255)),
                ('data_admissao', models.DateField()),
                ('data_demissao', models.DateField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='escola.user')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
                'db_table': 'professor',
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255)),
                ('matricula', models.CharField(max_length=255)),
                ('data_matricula', models.DateField()),
                ('data_cancelamento', models.DateField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.turma')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='escola.user')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'db_table': 'aluno',
            },
        ),
    ]
