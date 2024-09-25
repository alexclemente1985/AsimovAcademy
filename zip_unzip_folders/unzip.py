import shutil
from pathlib import Path


def unzip():
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'

    pasta_a_compactar = arquivos / 'pasta_teste_zip_unzip'
    nome_arquivo = arquivos / 'compactado.zip'
    pasta_descomp = arquivos / 'descompactada'

    # Compactando arquivo
    shutil.unpack_archive(nome_arquivo, pasta_descomp, 'zip')


unzip()
