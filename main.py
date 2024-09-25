import os
from pathlib import Path
def manipulacao_arquivos():
    #caminho = Path('arquivos/pasta_teste')
    caminho = Path('arquivos') / Path('pasta_teste')
    print(caminho)
    print(type(caminho))

    for nome in ['arquivo1.txt','arquivo2.txt','arquivo3.txt']:
        caminho_arquivo = caminho / nome
        print('caminho_arquivo ', caminho_arquivo)

    print("Path home -> outra pasta", Path.home() / 'outra_pasta')

    #Caminhos absolutos e caminhos relativos

    # True pq a inicialização está na mesma pasta que 'arquivos'
    print(Path('arquivos').exists())
    # False pq não está na mesma pasta da inicialização
    print(Path('pasta_teste').exists())

    print('Informar diretório atual -> ',Path.cwd())

    #Manipulação de caminhos de arquivos
    print('Caminho é absoluto? ', Path.cwd().is_absolute())

    print('Caminho não vai ser absoluto...', Path('pasta_teste').is_absolute())

    # Caminhos relativos podem dar problema... usar sempre os absolutos
    print(Path.cwd() /'arquivos' /'pasta_teste')
    print((Path.cwd() /'arquivos' /'pasta_teste').exists())

    # Trocando a pasta home do projeto com caminho absoluto (Não recomendada)
    os.chdir(Path.home())
    print(Path.cwd() / 'arquivos' / 'pasta_teste')
    print((Path.cwd() / 'arquivos' / 'pasta_teste').exists())

    # Forma correta

    # Garantia de que estamos retornando o caminho para a pasta do script
    print(__file__)
    print(Path(__file__))
    print(Path(__file__).is_absolute())

    # Retorno da pasta onde está contido o script
    print(Path(__file__).parent)
    print((Path(__file__).parent / 'arquivos'/'pasta_teste').exists())

    # Trabalhando com partes do arquivo
    caminho_arquivo = Path(__file__)

    # retorna a pasta raiz do disco rígido do computador
    print(caminho_arquivo.anchor)
    # retorna a pasta onde o arquivo de script está contido
    print(caminho_arquivo.parent)
    # retorna pastas acima da parent
    print(caminho_arquivo.parent.parent)

    # retorna nome do arquivo de script
    print(caminho_arquivo.name)
    # retorna nome do arquivo sem a extensão
    print(caminho_arquivo.stem)
    # retorna a extensão do arquivo
    print(caminho_arquivo.suffix)
    # retorna o nome do disco no computador
    print(caminho_arquivo.drive)

    # permite retorno mais fácil para pastas anteriores à parent (pasta [0])
    print(caminho_arquivo.parents[0])
    print(caminho_arquivo.parents[1])
    print(caminho_arquivo.parents[2])

    # Retorno de conteúdos de uma pasta
    print(os.listdir(Path.home()))
    # Mesmo retorno acima, mas como tipo Path e como caminhos absolutos (por causa do glob)
    print(list(Path.cwd().glob('*')))
    # Retornando somente os arquivos .py
    print(list(Path.cwd().glob('*.py')))

    # Retornando TUDO que tem dentro da pasta (inclusive outras pastas)
    # print(list(Path.cwd().glob('**/*.py')))

    # Validando caminhos
    nao_existe = Path.home() /'nao_existe'
    print(nao_existe.exists())

    # Verificando se é arquivo ou pasta
    print(Path(__file__).is_file())
    print(Path(__file__).is_dir())
    print(Path(__file__).parent.is_file())
    print(Path(__file__).parent.is_dir())

    ## Módulo 2 Copiando e movendo arquivos

    ### Copiando arquivo com copyfile
    pasta_atual = Path(__file__).parent
    caminho_arq2 = pasta_atual / 'texto.txt'
    ### Copiando arquivo com copy
    ### Copiando arquivo com copy2
    ### Movendo arquivos
    ### Deletando arquivos


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manipulacao_arquivos()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
