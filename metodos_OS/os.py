from pathlib import Path

import os

def metodos_os():
    print("OS.getcwd(): ",os.getcwd())
    print("OS.listdir(): ", os.listdir())
    print("OS.listdir(diretorio): ", os.listdir(Path(__file__).parents[3]))

    actual_dir = os.getcwd()
    #print("OS.chdir()", os.chdir(Path(__file__).parents[3]))
    #print("OS.getcwd(): ", os.getcwd())

    #os.mkdir('pasta_teste')
    #os.mkdir('pasta_teste_3')

    #os.rename('./arquivos/teste.txt', './arquivos/teste2.txt')

    #os.rename('pasta_teste','pasta_teste_3/pasta_teste2')
    #os.rename('pasta_teste_3/pasta_teste2', 'pasta_teste')

    #os.remove('./arquivos/teste.csv')

    #os.rmdir('pasta_teste_3')

    #Execução de comandos com o system
    #cmd = "date"

    #print("os.system() ", os.system(cmd))

if __name__ == '__main__':
    metodos_os()