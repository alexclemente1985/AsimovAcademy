# This is a sample Python script.
from comparacao import comparacao
from compreensao_listas import compreensao_listas
from condicionais import condicionais
from dicionarios import dicionarios
from exercicios_pt4_1 import exercicios_pt4_1
from exercicios_pt4_2 import exercicios_pt4_2
from funcoes import funcoes
from input_set_bool import input_set_bool
from listas import listas
from range_for_while import range_for_while
from tuplas import tuplas


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def python_starter():
    # Use a breakpoint in the code line below to debug your script.
    aula = input("Informe a aula: ")

    try:
        match int(aula):
            case 1:
                listas()
            case 2:
                dicionarios()
            case 3:
                tuplas()
            case 4:
                input_set_bool()
            case 5:
                comparacao()
            case 6:
                exercicios_pt4_1()
            case 7:
                condicionais()
            case 8:
                range_for_while()
            case 9:
                compreensao_listas()
            case 10:
                funcoes()
            case 11:
                exercicios_pt4_2()
            case _:
                print("Aula não encontrada")
    except ValueError:
        print("Valor inválido: não é número")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    python_starter()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
