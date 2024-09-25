import pandas as pd
from pathlib import Path

def lendo_escrevendo_planilhas():
    folder = Path.joinpath(Path.cwd(),'arquivos_mod3')

    #Lendo tabelas com DataFrame
    tabela_clientes = pd.read_excel(Path.joinpath(folder,'clientes.xlsx'))
    print(tabela_clientes)

    #Lendo aba específica
    aba_tabela_cliente = pd.read_excel(Path.joinpath(folder,'clientes.xlsx'),sheet_name='SC')
    print('\n15---------ABA ESPECÍFICA----------')
    print(aba_tabela_cliente.head(10))

    #Modificando header
    aba_tabela_cliente_sem_header = pd.read_excel(Path.joinpath(folder, 'clientes.xlsx'), sheet_name='SC', header=1)
    print('\n---------ALTERAÇÃO DO HEADER----------')
    print(aba_tabela_cliente_sem_header.head(10))

    #Adicionando coluna de index
    aba_tabela_cliente_col_idx = pd.read_excel(Path.joinpath(folder, 'clientes.xlsx'), sheet_name='SC', index_col=0)
    print('\n---------CRIAÇÃO DE COLUNA DE ÍNDICE----------')
    print(aba_tabela_cliente_col_idx.head(10))

    #Lendo colunas específicas
    aba_tabela_cliente_col_esp = pd.read_excel(Path.joinpath(folder, 'clientes.xlsx'), sheet_name='SC', usecols=[0,1])
    print('\n---------LEITURA DE COLUNAS ESPECÍFICAS----------')
    print(aba_tabela_cliente_col_esp.head(10))

    #Comentários sobre decimals e thousands -> decimal="." indica que a notação de decimais da planilha é representada por "."
    aba_tabela_cliente_leitura_dec = pd.read_excel(Path.joinpath(folder, 'clientes.xlsx'), decimal=".")
    print('\n---------VALORES DECIMAIS----------')
    print(aba_tabela_cliente_leitura_dec.head(10))
    # -> Quebra de milhares: representada por "." nesse caso (thousand) -> pode causar erros se usado indevidamente com o caso acima
    aba_tabela_cliente_leitura_milhares = pd.read_excel(Path.joinpath(folder, 'clientes.xlsx'), thousands=".")
    print('\n---------VALORES DE MILHARES----------')
    print(aba_tabela_cliente_leitura_milhares.head(10))

    #Escrevendo Planilha
    tabela_clientes_leitura = pd.read_excel(Path.joinpath(folder, 'clientes.xlsx'))
    if not Path.joinpath(folder,'exportacoes').exists():
        Path.mkdir(Path.joinpath(folder, 'exportacoes'))
    print('\n---------ESCRITA DE PLANILHA----------')
    tabela_clientes_leitura.to_excel(Path.joinpath(folder, 'exportacoes', 'copia_clientes.xlsx'))

    tabela_clientes_exportada = pd.read_excel(Path.joinpath(folder, 'exportacoes', 'copia_clientes.xlsx'),)
    print(tabela_clientes_exportada.head(10))

    #Escrevendo diversas abas
    print('\n---------ESCRITA DE VÁRIAS PLANILHAS----------')
    tabela_clientes_leitura_rs = pd.read_excel(Path.joinpath(folder, 'clientes.xlsx'),sheet_name='RS')
    tabela_clientes_leitura_sc = pd.read_excel(Path.joinpath(folder, 'clientes.xlsx'), sheet_name='SC')

    with pd.ExcelWriter(Path.joinpath(folder, 'exportacoes', 'copia_clientes.xlsx')) as nova_planilha:
        #Evita de adicionar a coluna de índice repetidas vezes
        tabela_clientes_leitura_rs.to_excel(nova_planilha, sheet_name='RS', index=False)
        tabela_clientes_leitura_sc.to_excel(nova_planilha, sheet_name='SC', index=False)


lendo_escrevendo_planilhas()