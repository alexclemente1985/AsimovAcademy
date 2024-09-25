from pathlib import Path
import shutil

def copy_files():

    # Copiando arquivo com copyfile (não copia permissões do arquivo original)
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'
    caminho_arquivo = arquivos/'texto_copy.txt'
    caminho_arq_dest = arquivos / 'destino1' / 'texto_copy.txt'

    if not (caminho_arq_dest/'texto_copy.txt').exists():
        shutil.copyfile(caminho_arquivo, caminho_arq_dest)


    # Copiando arquivo com copy (mantém as permissões do arquivo... não precisa informar nome do arquivo)
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'
    caminho_arquivo = arquivos / 'texto_copy.txt'
    caminho_arq_dest_2 = arquivos / 'destino2'

    if not (caminho_arq_dest_2/'texto_copy.txt').exists():
        shutil.copy(caminho_arquivo, caminho_arq_dest_2)


    # Copiando arquivo com copy2 (além das permissões tbm copia os metadados do arquivo)
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'
    caminho_arquivo = arquivos / 'texto_copy.txt'
    caminho_arq_dest_3 = arquivos / 'destino3'

    if not (caminho_arq_dest_3/'texto_copy.txt').exists():
        shutil.copy2(caminho_arquivo, caminho_arq_dest_3)


    # Copiando arquivos para teste de remoção de arquivos
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'
    caminho_arquivo = arquivos / 'texto_del.txt'
    caminho_arq_dest_3 = arquivos / 'destino3'

    if not (caminho_arq_dest_3/'texto_del.txt').exists():
        shutil.copy(caminho_arquivo, caminho_arq_dest_3)



copy_files()