def exercicios_pt4_2():
    print("<<<Exercício 1>>>")

    try:
        nota_1 = float(input("Informe a primeira nota do aluno: "))
        nota_2 = float(input("Informe a segunda nota do aluno: "))

        media = (nota_1+nota_2)/2

        if(media < 7):
            print("Reprovado")
        elif(media >=7 and media <10):
            print("Aprovado")
        else:
            print("Aprovado com Distinção")
    except:
        print("Valor incorreto para uma das notas do aluno")

    print("<<<Exercício 2>>>")

    try:
        a = int(input("Informe um número: "))
        b = int(input("Informe outro número: "))
        c = int(input("Informe outro número: "))

        lista = [a,b,c]
        maior = -9*10e99
        menor = 9*10e99
        for i in lista:

            if(i > maior):
                maior = i
            if(i < menor):
                menor = i

        print(f"Maior número: {maior} | Menor número: {menor}")
    except:
        print("Valor incorreto inserido para número")

    print("<<<Exercício 3>>>")

    nome = "Fulano"
    def escada_com_nome(nome):
        concatenacao = ''
        for i in nome:
            concatenacao += i.upper()
            print(concatenacao)

    escada_com_nome(nome)

    print("<<<Exercício 4>>>")

    def fibo(n):
        try:
            fibonacci = list()
            for i in range(n):
                if i == 0 or i == 1:
                    fibonacci.append(1)
                else:
                    valor = fibonacci[-2] + fibonacci[-1]
                    fibonacci.append(valor)

            return fibonacci
        except Exception as e:
            print("Erro no fibonacci: ", e)

    print("Lista de fibonacci para 10 números: \n")
    print(fibo(10))

    print("<<<Exercício 5>>>")

    def validador(nome, idade, salario, sexo, estado):
        validacao = True
        def altera_validacao(v):
            if v == False:
                return False
            else:
                return True

        if len(nome)<3:
            print("Valor de nome com caracteres insuficientes")
            if altera_validacao(validacao):
                validacao = False
        if idade<0 or idade>150:
            print("Valor de idade inválido para o programa")
            if altera_validacao(validacao):
                validacao = False
        if salario<=0:
            print("Valor de salário inválido")
            if altera_validacao(validacao):
                validacao = False

        if sexo.lower() != 'f' and sexo.lower() != 'm':
            print("Valor de sexo inválido")
            if altera_validacao(validacao):
                validacao = False
        if estado.lower() != 's' and estado.lower() != 'c' and estado.lower() != 'v' and estado.lower() != 'd':
            print("Valor de estado civil inválido")
            if altera_validacao(validacao):
                validacao = False
        if validacao:
            print("Dados validados e considerados corretos")
        else:
            print("Revisar os dados inseridos e enviar novamente...")

    print("------Validação 1------")
    validador('Alexandre', 38, 2000, 'm','s')
    print("------Validação 2------")
    validador('Al',38, 2000, 'm','s')
    print("------Validação 3------")
    validador('Ale', 151, 2000, 'm', 's')
    print("------Validação 4------")
    validador('Alexa', 38, 0, 'f', 's')
    print("------Validação 5------")
    validador('Alexa', 38, 2000, 'p', 'c')
    print("------Validação 6------")
    validador('Alexa', 38, 2000, 'f', 'e')
    print("------Validação 7------")
    validador('Al', -8, 0, 'h', 'l')


    print("<<<Exercício 6>>>")

    def verifica_num_primo():
        try:
            numero = int(input("Informe um número para ver se ele é primo: "))

            lista_verif = [n for n in range(2,numero) if numero % n == 0]

            if len(lista_verif) > 0:
                print(f"{numero} não é um número primo")
            else:
                print(f"{numero} é um número primo")
        except:
            print("Valor inválido para número")

    verifica_num_primo()