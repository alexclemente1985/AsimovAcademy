import os
import shutil
import time
from pathlib import Path


def del_files():
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'
    caminho_arquivo = arquivos / 'destino3'/ 'texto_del.txt'

    if caminho_arquivo.exists():
        os.remove(caminho_arquivo)


del_files()