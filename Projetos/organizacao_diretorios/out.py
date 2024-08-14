import os
from pathlib import Path


def out_method():
    #Para o caso do script ser executado dentro da pasta a ser organizada
    #cwd = os.getcwd()
    cwd = Path(__file__).parent / 'arquivos_teste'

    #Obtenção da lista de pastas criadas pelo script "in"
    #Para o caso do script estar no interior da pasta organizada
    #folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]
    folder_list = [i for i in os.listdir(cwd) if os.path.isdir(os.path.join(cwd,i))]

    for folder in folder_list:
        #Cria o caminho para cada pasta criada
        path = os.path.join(cwd, folder)

        #Lista os arquivos de cada pasta
        files = os.listdir(path)
        for file in files:
            from_path = os.path.join(path, file)
            to_path = os.path.join(cwd, file)

            os.replace(from_path, to_path)

        os.rmdir(path)


if __name__ == '__main__':
    out_method()