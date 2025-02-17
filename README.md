# Sistema de Gestão Escolar

Sistema de gestão escolar desenvolvido com Django e Django REST Framework.

## Requisitos

- Python 3.13+
- PDM (Python Dependency Manager)

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone https://github.com/jonatasperaza/Avaliacao_PI
cd Avaliacao_PI
```

2. Instale o PDM (caso não tenha):
```bash
pip install pdm
```

3. Instale as dependências:
```bash
pdm install
```

4. Execute as migrações:
```bash
pdm migrate
```

5. Crie um superusuário:
```bash
pdm createsuperuser
```

## Rodando o Projeto

Para iniciar o servidor de desenvolvimento:
```bash
pdm runserver
```

O servidor estará disponível em: http://127.0.0.1:8000/

## API Endpoints

### Usuários
- Lista/Criar: `/api/users/`
- Detalhes/Atualizar/Deletar: `/api/users/{id}/`

### Alunos
- Lista/Criar: `/api/alunos/`
- Detalhes/Atualizar/Deletar: `/api/alunos/{id}/`

### Professores
- Lista/Criar: `/api/professores/`
- Detalhes/Atualizar/Deletar: `/api/professores/{id}/`

### Escolas
- Lista/Criar: `/api/escolas/`
- Detalhes/Atualizar/Deletar: `/api/escolas/{id}/`

### Turmas
- Lista/Criar: `/api/turmas/`
- Detalhes/Atualizar/Deletar: `/api/turmas/{id}/`

## Exemplos de Uso

### Criando um Professor
```json
POST /api/professores/
{
    "user": {
        "username": "professor1",
        "password": "senha123",
        "email": "prof@escola.com",
        "first_name": "Professor",
        "last_name": "Silva",
        "data_nascimento": "1980-01-01"
    },
    "formacao": "Matemática",
    "especialidade": "Álgebra"
}
```

### Criando um Aluno
```json
POST /api/alunos/
{
    "user": {
        "username": "aluno1",
        "password": "senha123",
        "email": "aluno@escola.com",
        "first_name": "Aluno",
        "last_name": "Santos",
        "data_nascimento": "2000-01-01"
    },
    "matricula": "2024001",
    "data_matricula": "2024-01-01",
    "turma": 1
}
```

## Comandos Úteis

| Comando | Descrição |
|---------|-----------|
| `pdm migrate` | Aplica migrações pendentes |
| `pdm makemigrations` | Cria novas migrações |
| `pdm createsuperuser` | Cria usuário administrador |
| `pdm runserver` | Inicia servidor de desenvolvimento |
| `pdm test` | Executa testes |
| `pdm model` | Gera diagrama de modelos |
| `pdm req` | Exporta requirements.txt |

## Estrutura do Projeto

```
Avaliacao_PI/
├── core/
│   └── escola/
│       ├── models/
│       ├── serializers/
│       └── views/
├── config/
└── manage.py
```

## Licença

MIT
