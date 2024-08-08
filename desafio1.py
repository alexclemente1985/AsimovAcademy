import os
from pathlib import Path

def desafio1():

    #Desenvolver função para retornar o tamanho dos diretórios
    caminho = Path.cwd().parent.parent
    retorna_tamanho_dir(caminho, profundidade=3)


def retorna_tamanho_dir(caminho, profundidade=1, tamanho_linha=0):

    #Pega somente a camada inicial (profundidade 1) das pastas
    for diretorio in caminho.glob('*'):
        #Verifica quem é pasta e se não é uma pasta oculta
        if diretorio.is_dir() and not diretorio.name.startswith('.'):
            tamanho_dir = 0
            #Verifica todos os arquivos dentro da pasta da vez (inclusive em pastas filhas)
            for arquivo in diretorio.glob('**/*'):
                if arquivo.is_file():
                    #Soma o tamanho de cada arquivo da vez na variável tamanho_dir
                    tamanho_dir += os.path.getsize(arquivo)
            #Imprime '--' multiplicado por cada nível de pasta, nome das pastas e tamanho convertido em MB
            print('--'*tamanho_linha, diretorio.name, round(tamanho_dir / 1024 / 1024), 'mb')

            #Possibilita recursividade, aumentando o número de '--' a cada profundidade alcançada
            if profundidade > 1:
                retorna_tamanho_dir(diretorio, profundidade-1, tamanho_linha+1)


if __name__ == '__main__':
    desafio1()