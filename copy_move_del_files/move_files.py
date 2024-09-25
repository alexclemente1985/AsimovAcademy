import shutil
from pathlib import Path


def move_files():

    # Movendo arquivos
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'
    caminho_arquivo = arquivos / 'texto_move.txt'
    caminho_arq_dest = arquivos / 'destino1'

    shutil.move(caminho_arquivo, caminho_arq_dest)

    '''
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'
    caminho_arquivo = arquivos / 'texto_move.txt'
    caminho_arq_dest = arquivos / 'destino1/ 'texto_move.txt'

    shutil.move(caminho_arquivo, caminho_arq_dest)
    '''



move_files()