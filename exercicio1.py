from pathlib import Path

def encontra_arquivo(caminho, arquivo):
    for arq in caminho.glob('**/*'):
        if arq.is_file():
            if arq.stem == arquivo:
                print("Encontrei -> ", arq)
def exercicio1():

    caminho = Path.cwd()

    encontra_arquivo(caminho, 'arquivo1')
    encontra_arquivo(caminho, 'arquivo3')


if __name__ == '__main__':
    exercicio1()