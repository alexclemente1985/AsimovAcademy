import shutil
from pathlib import Path


def zip():
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'

    pasta_a_compactar = arquivos / 'pasta_teste_zip_unzip'
    nome_arquivo = arquivos /  'compactado'

    # Compactando arquivo
    shutil.make_archive(nome_arquivo, 'zip', pasta_a_compactar)

zip()