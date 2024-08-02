import math


def exercicios_pt4_1():
    print("Exercício IMC:")
    try:
        altura = float(input("Informe sua altura: \n"))
        peso = float(input("Informe o seu peso: \n"))

        imc = peso / (altura) ** 2
        print("Seu imc é: ", imc)
    except Exception as e:
        print("Valor inserido para peso ou altura não é válido")

    print("Exercício saudação pelo nome completo:")

    nome = input("Por favor informe o seu nome completo: \n")
    print(f"Prazer em conhecê-lo, {nome}")

    print("Exercício de extração de domínio de email: ")

    email = input("Informe o email: \n")

    try:
        dominio = email.split('@')[1]
        print(f"Domínio do email: {dominio}")
    except:
        print("Email inválido!")

    print("<<<Exercício loja de tintas>>>")

    try:
        area = float(input("Informe a área em m2 que deseja pintar: \n"))

        capacidade_litro = 3
        volume_lata = 18
        valor_lata = 80

        qtd_latas = math.ceil(area/(capacidade_litro*volume_lata))
        valor_total = qtd_latas*valor_lata

        print(f"Quantidade de latas a serem compradas: {qtd_latas} | Valor total: {valor_total}")
    except:
        print("Valor inválido para área!")

    print("<<<Exercício Horas Trabalhadas e Salário>>>")

    try:
        ganho_hora = float(input("Informe o seu valor de ganho por hora: \n"))
        horas_trabalhadas = int(input("Informe o total de horas trabalhadas no mês: \n"))

        irpf = 0.11
        inss = 0.08
        sindicato = 0.05

        salario_bruto = ganho_hora*horas_trabalhadas
        gasto_irpf = salario_bruto * irpf
        salario_liq_parcial = salario_bruto - gasto_irpf
        gasto_inss = inss*salario_liq_parcial
        gasto_sindicato = sindicato*salario_liq_parcial


        salario_liquido = salario_liq_parcial - gasto_sindicato - gasto_inss

        print(f"Informações do trabalhador:")
        print(f"Salario bruto: {salario_bruto}")
        print(f"Gasto INSS: {gasto_inss}")
        print(f"Gasto sindicato: {gasto_sindicato}")
        print(f"Salário líquido: {salario_liquido}")
    except:
        print("Valores inválidos de ganho por hora ou de horas trabalhadas!")

if __name__ == '__main__':
    exercicios_pt4_1()
