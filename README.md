# README

## Informações Úteis

### Criando ambiente virtual venv manualmente (pasta raiz do projeto):
`python3 -m venv .venv`

### Ativando o ambiente virtual criado:
- macOS/Linux:
  `source .venv/bin/activate`
- Windows:
  `.venv\Scripts\activate`

### Verificando a ativação do ambiente virtual
- macOS/Linux:
  `which python`
- Windows:
  `where python`

### Caminho para o python do venv:
- macOS/Linux:
  `.venv/bin/python`
- Windows:
  `.venv\Scripts\python`

### Desativando o ambiente virtual venv
`deactivate`

### Instalando libs a partir de requirements.txt:
`pip install -r requirements.txt`

### Criando arquivo de requirements.txt a partir das libs já instaladas:
`pip freeze > requirements.txt`


### Criando projeto Django
`django-admin startproject <nome_do_projeto>`

### Criando app Django
`python3 manage.py startapp <NOME_APP>`
- Integrar o projeto em settings -> installed apps

### Rodando o server Django
- Iniciar o arquivo gerado pelo comando anterior
`python3 manage.py runserver` ou `python manage.py runserver`