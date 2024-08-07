from AsimovAcademy.Projetos.Calculadora.funcoes.info_escolha import info_escolha
from AsimovAcademy.Projetos.Calculadora.funcoes.menu import menu
from AsimovAcademy.Projetos.Calculadora.funcoes.operação import operacao
import os

#from Projetos.Calculadora.funcoes.info_escolha import info_escolha
#from Projetos.Calculadora.funcoes.menu import menu
#from Projetos.Calculadora.funcoes.operação import operacao


def calculadora():
    print("========")

    continua = True

    while continua:
        #Limpeza de tela
        #os.system("clear")

        menu()

        operador = info_escolha()

        try:
            valor_1 = float(input("Qual o primeiro valor?\n"))
            valor_2 = float(input("Qual o segundo valor?\n"))

            operacao(valor_1, valor_2, operador)

            continuar = input("Digite 'S' para continuar calculando (ou qualquer tecla para encerrar)")
            continua = continuar.upper() == "S"
        except:
            print("Valor(es) incorreto(s) informado(s)... informe novamente\n")
            continue

    else:
        print("Programa encerrado com sucesso!")



if __name__ == '__main__':
    calculadora()
