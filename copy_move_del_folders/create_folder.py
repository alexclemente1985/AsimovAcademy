import shutil
from pathlib import Path


def create_folder():
    pasta_raiz = Path(__file__).parents[1]
    arquivos = pasta_raiz / 'arquivos'
    caminho_pasta_destino4 = arquivos / 'destino4'

    #Cria pasta caso a mesma não exista ainda
    caminho_pasta_destino4.mkdir(exist_ok=True)

    #Cria pasta com todas as anteriores necessárias
    caminho_pasta_destino5_5_1 = arquivos/ 'destino5'/'destino5_1'
    caminho_pasta_destino5_5_1.mkdir(parents=True, exist_ok=True)

    # Criando pasta para teste de remoção
    caminho_pasta_destino6 = arquivos / 'destino6'
    caminho_pasta_destino6.mkdir(exist_ok=True)
    caminho_arquivo_teste = arquivos/ 'texto_remover_pasta.txt'
    if not (caminho_pasta_destino6 / 'texto_remover_pasta.txt').exists():
        shutil.copy(caminho_arquivo_teste, caminho_pasta_destino6)



create_folder()