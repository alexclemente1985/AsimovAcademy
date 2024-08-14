from datetime import datetime

import os


def os_path():
    os.getcwd()
    concatenacao = os.path.join(os.getcwd(), 'pasta')
    #concatenacao = os.getcwd() + '/pasta'

    print(concatenacao)

    ultima_pasta = os.path.basename(os.getcwd())
    print(ultima_pasta)

    split_fim = os.getcwd().split('/')[-1]
    split_parte_final = os.path.split(os.getcwd())[1]
    split_duas_partes = os.path.split(os.getcwd())
    split_inicio = os.path.dirname(os.getcwd())

    print("testes split: ", split_inicio,'\n',split_parte_final,'\n', split_duas_partes,'\n', split_fim,'\n')

    curr_dir = os.getcwd()
    lt = os.path.getmtime(curr_dir)
    print("tempo sem ambiguidade (tempo da pasta): ", datetime.utcfromtimestamp(lt))

    print("Verificação do tipo: ", os.path.isfile(curr_dir), os.path.isdir(curr_dir))
if __name__ == '__main__':
    os_path()