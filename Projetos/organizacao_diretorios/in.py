import os
from pathlib import Path


def in_method():

    #pega o diretório corrente
    #cwd = os.getcwd()

    #pega o diretório desejado
    cwd = Path(__file__).parent / 'arquivos_teste'

    #lista conteúdo do diretório corrente
    full_list = os.listdir(cwd)

    #cria lista de arquivos a partir da lista anterior, excluindo os de python
    #files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]
    files_list = [i for i in full_list if os.path.isfile(os.path.join(cwd,i)) and '.py' not in i]

    #cria lista de tipos de arquivos em set (descarta repetições)
    types = set([i.split('.')[1] for i in files_list])

    #cria pasta para cada um dos tipos encontrados
    for file_type in types:
        #Exemplo professor (mesma pasta do script)
        #os.mkdir(file_type)

        #Para caso de pastas diferentes
        os.mkdir(os.path.join(cwd, file_type))
        #print('teste pastas: ',os.path.join(cwd, file_type) )

    for file in files_list:
        from_path = os.path.join(cwd, file)
        to_path = os.path.join(cwd, file.split('.')[-1], file)

        os.replace(from_path, to_path)
        #print("teste realocação arquivos: ", from_path, to_path)


if __name__ == '__main__':
    in_method()