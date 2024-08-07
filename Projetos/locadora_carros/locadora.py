#Etapas
#1) Implementar processo devolução veículo
#--> Alterar csv para registrar dias do aluguel
#--> Implementar módulo de devolução

#2) Implementar registro dos dados no csv ao encerrar o programa



import csv

# from Projetos.locadora_carros.recursos.database_dictionary import database_dictionary
# from Projetos.locadora_carros.recursos.menu_locadora import menu_locadora

import os
from pathlib import Path
import csv

from AsimovAcademy.Projetos.locadora_carros.recursos.alugar_veiculo import alugar_veiculo
from AsimovAcademy.Projetos.locadora_carros.recursos.database_dictionary import database_dictionary
from AsimovAcademy.Projetos.locadora_carros.recursos.menu_locadora import menu_locadora
from AsimovAcademy.Projetos.locadora_carros.recursos.portfolio import portfolio


def locadora():
    try:
        db_path = Path(__file__).parent / "recursos/db/carros.csv"

        database = csv.reader(open(db_path))
        dados = database_dictionary(database)

        escolha = menu_locadora()

        while escolha in [0, 1, 2]:
            match escolha:
                case 0:
                    portfolio(0, dados)
                case 1:
                    dados = alugar_veiculo(dados)
                case 2:
                    continue

            continuar = input("Deseja algo mais (Digite 'S' para sim ou qualquer tecla para encerrar o programa)?\n")

            if continuar.upper() == 'S':
                escolha = menu_locadora()
            else:
                escolha = -1
        else:
            print("Finalizando o programa")

    except Exception as e:
        print("Erro na execução do programa: ", e)


if __name__ == '__main__':
    locadora()
