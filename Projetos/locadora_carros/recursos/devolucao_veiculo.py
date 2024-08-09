import copy
from typing import List, Dict

from AsimovAcademy.Projetos.locadora_carros.recursos.portfolio import portfolio


def devolucao_veiculo(veiculos: List[Dict]):
    def reset(v_dev: List[Dict], v_dev_bkp: List[Dict], index_list: List[int], mostrar_port: bool = True):
        altera_lista_veiculos(v_dev, v_dev_bkp, False)
        if mostrar_port:
            portfolio(2, veiculos)

        index_list.clear()

    def altera_lista_veiculos(veiculos_1, veiculos_2, mostra_msg: bool = True):
        for v_1 in veiculos_1:
            for v_2 in veiculos_2:
                if int(v_1['index']) == int(v_2['index']):
                    v_1['disponivel'] = v_2['disponivel']
                    v_1['tempo'] = v_2['tempo']
        if mostra_msg:
            print("Veículos devolvidos com sucesso.")


    portfolio(2, veiculos)

    index_list = list()
    achou_index = False

    veiculos_dev = [v for v in veiculos if not bool(v['disponivel'])]
    veiculos_dev_bkp = copy.deepcopy(veiculos_dev)

    if len(veiculos_dev) == 0:
        print("Sem veículos para serem devolvidos.")
        return veiculos

    while True:
        try:
            if achou_index:
                achou_index = False

            index = int(input("Escolha o código do veículo a ser devolvido?\n"))

            for v in veiculos_dev:
                for v_bkp in veiculos_dev_bkp:
                    if index == int(v['index']) and v_bkp['index'] == v['index'] and v_bkp['disponivel'] == v['disponivel']:
                        v['disponivel'] = True
                        v['tempo'] = 0
                        achou_index = True
                        index_list.append(index)

            if not achou_index:
                print("Valor de código não encontrado. Insira novamente.")
                continue
            else:

                i = len(index_list)

                if i < len(veiculos_dev):
                    continua = input("Deseja devolver outro veículo (S para sim | qualquer tecla para não)?\n")

                    if continua.upper() == 'S':
                        portfolio(2, veiculos_dev)
                        continue
                    else:
                        continua = input(
                            "Todos os veículos marcados serão devolvidos. Deseja confirmar devolução (S para sim | "
                            "qqr tecla para não)")
                        if continua.upper() == 'S':
                            altera_lista_veiculos(veiculos, veiculos_dev)
                            return veiculos
                        else:
                            reset(veiculos_dev, veiculos_dev_bkp, index_list, False)
                            continua = input("Deseja continuar na tela de devolução (S para sim | qqr tecla para não)")
                            if continua.upper() == 'S':
                                portfolio(2, veiculos)
                                continue
                            else:
                                return veiculos
                else:
                    continua = input(
                        "Todos os veículos já foram marcados para serem devolvidos. Deseja confirmar devolução (S "
                        "para sim | qqr tecla para não)")
                    if continua.upper() == 'S':
                        altera_lista_veiculos(veiculos, veiculos_dev)
                        return veiculos
                    else:
                        reset(veiculos_dev, veiculos_dev_bkp, index_list, False)
                        continua = input("Deseja continuar na tela de devolução (S para sim | qqr tecla para não)")
                        if continua.upper() == 'S':
                            portfolio(2, veiculos)
                            continue
                        else:
                            return veiculos


        except:
            print("Valor incorreto para código de veículo ")
