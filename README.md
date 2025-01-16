# Organizador pasta downloads (aula Asimov)

## Script para organizar a pasta de downloads periodicamente

## Informações para agendamentos

### Mac e Linux

#### Uso do crontab e VIM (editor do crontab)
- Consultar <www.crontab.guru>
- Consultar comandos **VIM** no arquivo **_cron_linux_mac.pdf_**

##### Listagem de scripts em uma pasta
`crontab -l`

##### Criação de crontab (abrirá o VIM)
`crontab -e`

###### Comandos no VIM
- `<inserir as condições de execução (vide www.crontab.guru)> cd <Inserir o caminho da pasta do arquivo cron.py> && <inserir caminho python global> **cron.py**`
- Salvar e sair (digitar `:wq` no editor)
- Processo de criação de crontab será automático após fechamento do VIM



### Windows
#### Usar agendador de tarefas
- Clicar em ação -> criar tarefa
- GERAL: Dar o nome da tarefa e outras informações (sugestão: deixar para Windows 10 e usuário atual)
- DISPARADORES: Definir as condições da execução da tarefa (se vai ser na inicialização, desligamento, etc. No caso, foi escolhida a condição **"Ao bloquear estação"** )
- AÇÕES: 
    - Manter a Ação **"Iniciar um programa"**;
    - Em **"Programa/script"**, inserir o caminho para a instalação global python (inserir no terminal o comando abaixo)
        - `python -c "import sys; print(sys.executable)"`
    - Em **"Iniciar em (opcional)"**, colocar o caminho da pasta onde se encontra o arquivo python com o código a ser executado
    - Em **"Adicione argumentos (opcional)"**, coloque o nome do arquivo (com a extensão)
    - As demais abas possuem configurações não utilizadas para o teste em questão (manutenção do estado padrão)


## Informações Úteis (Desenvolvimento)

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