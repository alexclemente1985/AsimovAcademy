import shutil
from pathlib import Path


def copy_folder():
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'

    # Copiando pastas
    shutil.copytree(arquivos/'destino5', arquivos/'destino4'/'destino5')

copy_folder()