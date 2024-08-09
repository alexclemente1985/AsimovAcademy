#Etapas

#2) Implementar registro dos dados no csv ao encerrar o programa



# from Projetos.locadora_carros.recursos.menu_locadora import menu_locadora

import os
from pathlib import Path
import csv

from AsimovAcademy.Projetos.locadora_carros.recursos.alugar_veiculo import alugar_veiculo
from AsimovAcademy.Projetos.locadora_carros.recursos.db.escrita_arquivo import escrita_arquivo
from AsimovAcademy.Projetos.locadora_carros.recursos.db.leitura_arquivo import leitura_arquivo
from AsimovAcademy.Projetos.locadora_carros.recursos.devolucao_veiculo import devolucao_veiculo
from AsimovAcademy.Projetos.locadora_carros.recursos.menu_locadora import menu_locadora
from AsimovAcademy.Projetos.locadora_carros.recursos.portfolio import portfolio


def locadora():
    try:
        db_path = Path(__file__).parent / "recursos/db/carros.txt"

        dados = leitura_arquivo(db_path)

        escolha = menu_locadora()

        while escolha in [0, 1, 2]:
            match escolha:
                case 0:
                    portfolio(0, dados)
                case 1:
                    dados = alugar_veiculo(dados)
                case 2:
                    dados = devolucao_veiculo(dados)

            continuar = input("Deseja algo mais (Digite 'S' para sim ou qualquer tecla para encerrar o programa)?\n")

            if continuar.upper() == 'S':
                escolha = menu_locadora()
            else:
                escolha = -1
        else:
            escrita_arquivo(db_path, veiculos=dados)
            print("Finalizando o programa")

    except Exception as e:
        print("Erro na execução do programa: ", e)


if __name__ == '__main__':
    locadora()
