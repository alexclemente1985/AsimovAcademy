from typing import List, Dict

from AsimovAcademy.Projetos.locadora_carros.recursos.menu_locadora import menu_locadora
from AsimovAcademy.Projetos.locadora_carros.recursos.portfolio import portfolio


def calculo_aluguel(veiculo: Dict, dias: int) -> bool:
    print(f"Você escolheu {veiculo['nome']} por {dias} dias.")
    confirmacao = input(
        f"O aluguel totalizaria R$ {dias * int(veiculo['diaria'])}. Deseja alugar (digite 'S' para sim e qualquer tecla para não)?")

    return confirmacao.upper() == 'S'


def alugar_veiculo(veiculos: List[Dict]):
    portfolio(1, veiculos)

    try:
        print("========")
        prosseguir = False
        veiculo = dict()

        veiculos_disp = [v for v in veiculos if bool(v['disponivel'])]

        while True:
            codigo = input("Escolha o código do carro:\n")

            for c in veiculos_disp:
                if codigo == c['index']:
                    veiculo = c
                    prosseguir = True
                    break

            if prosseguir:
                break
            else:
                print("Código não encontrado... tente novamente.")
                continue

        while True:
            try:
                dias = int(input("Escolha por quantos dias deseja alugar:\n"))
                confirmado = calculo_aluguel(veiculo, dias)

                if confirmado:
                    veiculo['disponivel'] = False
                    veiculo['tempo'] = dias

                    for v in veiculos:
                        if v['index'] == veiculo['index']:
                            v['disponivel'] = False
                            v['tempo'] = dias

                    print(f"Veículo {veiculo['nome']} alugado com sucesso! Duração do aluguel: {dias} dias.\n")

                return veiculos


            except:
                print("Valor inválido para período de aluguel... tente novamente.")

    except Exception as e:
        print("Erro na inserção da informação do veículo a ser alugado ou no valor da qtd de dias de aluguel. ", e)
