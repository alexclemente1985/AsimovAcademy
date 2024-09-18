from pathlib import Path


def lendo_escrevendo_texto():
    pasta_atual = Path(__file__).parent

    # Forma não recomendada de ler arquivo
    ## Precisa ficar lembrando de sempre fechar os arquivos abertos (pode haver esquecimento)

    lista_compras = open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras.txt'))
    print(lista_compras.read())
    lista_compras.close()
    ###
    print('Forma correta de ler: Com with open')
    # Forma recomendada de ler arquivo
    ##Fecha automaticamente no final do bloco do with
    ### mode = r (default)-> somente leitura | mode = r+ -> leitura e escrita (mas não cria nem sobrescreve)
    with open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras.txt'), mode='r') as lista_compras:
        print(lista_compras.read())

    # Leitura linha a linha
    with open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras.txt'), mode='r') as lista_compras:
        linha = lista_compras.readline()
        while linha != '':
            # Ocorre um espaço entre as linhas devido ao \n no final de cada linha; para remover, usar o parâmetro end=''
            print(linha, end='')
            linha = lista_compras.readline()

    print('')
    # Lendo todas as linhas
    with open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras.txt'), mode='r') as lista_compras:
        # Irá printar uma lista com os valores seguidos de \n
        print(lista_compras.readlines())

    # Escrita em arquivo
    itens_comprados = ['farinha', 'fermento', 'agua']

    with open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras.txt'), mode='r') as lista_compras:
        itens_lista = lista_compras.readlines()

    with open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras_atualizada.txt'),
              mode='w') as lista_atualizada:
        for item in itens_lista:
            if not item.replace('\n', '') in itens_comprados:
                lista_atualizada.write(item)

    # Escrita linha a linha:

    itens_comprados = ['farinha', 'fermento', 'agua']

    with open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras.txt'), mode='r') as lista_compras:
        itens_lista = lista_compras.readlines()

    itens_lista_atualizada = [item for item in itens_lista if not item.replace('\n', '') in itens_comprados]

    with open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras_atualizada2.txt'),
              mode='w') as lista_atualizada:
        lista_atualizada.writelines(itens_lista_atualizada)

    # Adicionando itens em uma lista -> append (modo 'a')

    novos_itens = ['maçã', 'goiaba']
    novos_itens_com_quebra = [f'\n{item}' for item in novos_itens]

    with open(Path.joinpath(pasta_atual, 'arquivos_mod3', 'lista_de_compras_atualizada2.txt'),
              mode='a') as lista_atualizada:
        lista_atualizada.writelines(novos_itens_com_quebra)


lendo_escrevendo_texto()
