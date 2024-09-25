import shutil
from pathlib import Path


def del_folder():
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'

    # Removendo pastas vazias
    pasta_remover = arquivos / 'destino5'/'destino5_1'
    if pasta_remover.exists():
        pasta_remover.rmdir()

    # Removendo pastas com conteúdo
    pasta_com_conteudo_remover = arquivos / 'destino6'
    if pasta_com_conteudo_remover.exists():
        shutil.rmtree(pasta_com_conteudo_remover)




del_folder()