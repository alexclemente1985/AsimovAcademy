from pathlib import Path


def desafio_html():
    file = Path.joinpath(Path.cwd().parent, 'arquivos', 'view_lista.html')
    exports_path = Path.joinpath(Path.cwd(), 'exportacoes')

    if not exports_path.exists():
        Path.mkdir(exports_path)

    updated_file = Path.joinpath(exports_path, 'view_lista_atualizada.html')

    item_remover = "Passear com cachorro"
    novas_linhas_html = []
    escrever_linha = True

    #Passo 1: carregamento das linhas do html original
    with open(file) as html:
        # Apesar de estar no escopo desse with, linhas_html continua disponível para o resto do código
        linhas_html = html.readlines()

    #Passo 2: Realizar o preenchimento do array da atualização html, excluindo o item_remover
    for i, linha in enumerate(linhas_html):
        #len(linhas_html)-3 permite que o bloco de if seja acionado somente até a antepenúltima linha do html original
        ## Essa condição se deve ao fato da formatação do html ter listas onde a descrição está 2 linhas abaixo da linha do atributo <li>
        if i < len(linhas_html) - 3 and item_remover in linhas_html[i + 2]:
            # Isso irá fazer com que quando houver o match das condições acima e achar o texto na linha i+2,
            ## o bloco do item da lista referente ao texto não apareça no html atualizado
            escrever_linha = False
        if escrever_linha:
            novas_linhas_html.append(linha)

        #Como logo após o texto a ser removido tem esse atributo html abaixo, o mesmo serve de padrão para reativar a escrita das linhas seguintes
        if '</li>' in linha:
            escrever_linha = True

    #Passo 3: criação do html atualizado
    with open(updated_file, mode='w') as html_upd:
        html_upd.writelines(novas_linhas_html)


desafio_html()
