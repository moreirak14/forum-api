# Forum API
Implementar uma API que servirá a uma aplicação web do tipo fórum livre, em que usuários poderão submeter novas perguntas ou questionamentos, assim como responder a perguntas existentes.

## Pré-requisitos

- Python 3.10+: `https://www.python.org/downloads/`
- Docker: `https://www.docker.com/`
- Poetry: `https://python-poetry.org/docs/#installation`

## Necessário

- Criar novo arquivo `.secrets.toml`: Será necessário copiar o arquivo `.
  example.secrets.toml` para `.secrets.toml`.
  - O `secret.toml` é onde localiza variaveis sensiveis da aplicação.
- Para criar automaticamente o arquivo mencionado:
`$ make copy-envs`

## Utilização em desenvolvimento local
O arquivo `Makefile` que existe na raiz do projeto, tem todos os comandos necessários mapeados.

- Para instalar todos os pacotes necessários e criar um ambiente virtual:
`$ poetry shell` ou `$ poetry install` ou `$ make setup`

- Para subir as migrações de database:
`$ python manage.py migrate` ou `$ make migrate`

- Para gerar uma nova migração de database:
`$ python manage.py makemigrations` ou `$ make makemigrations`

- Para executar a aplicação:
`$ python manage.py runserver` ou `$ make run`

## Documentação

O sistema contém documentação de API, será possivel analisar toda a
estrutura após inicializar o sistema e acessar à url:
`http://localhost:8000/swagger/` ou
`http://localhost:8000/redoc/`
