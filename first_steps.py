def first_steps():
    #print e números
    print("Olá, mundo")
    print(1+2)
    print(1 - 2)
    print(1 * 2)
    print(1 / 2)
    print(1 ** 2)
    print(type(1))
    print(type(0.5))

    #strings e variáveis
    texto = "Olá mundo"
    print(type(texto))
    print(texto)
    nome = "Alexandre"
    print(texto+", "+nome)

    pi = 3.14
    raio = 5
    raio_quadrado = raio**2
    print("Área do círculo de raio 5: ", pi * raio_quadrado)

    #Strings, listas e Slicing
    a ="Ola"
    b= 3
    c="Alex"

    ##Pegará a variável "c" e jogar dentro da string
    d = f"Teste de string: {a}, {c}"

    print(d)

    ##Listas
    lista = [a, b, c, "lista"]
    print(type(lista))
    print(lista[2])
    print(len(lista))
    print(lista[-1])

    ##Slice -> cortes na lista (última posição não inclusa)
    print(lista[1:3])

    print(len(c))
    print(c[0:2])

    #Booleanos e Operadores de Comparação
    print(type(True))
    print(3 > 2)
    booleano = 3 >= 4
    print(booleano)
    booleano = 2 <= 2
    print(booleano)
    booleano = 3 == 4
    print(booleano)
    booleano = 3 != 4
    print(booleano)

    print(True and True)
    print(False and True)
    print(True or True)
    print(True or False)

    #Estruturas de controle de fluxo

    idade = 18
    possui_carteira = True
    if(int(input("Informe a sua idade: \n")) >= idade and possui_carteira):
        print("Você pode dirigir")
    elif(possui_carteira):
        print("Você apenas possui carteira... espera completar a idade correta.")
    else:
        print("Você ainda não pode dirigir")

    #for
    for i in lista:
        print(f"Valor na lista: {i}")

    a = ''
    for x in ['a ', 'frase ', 'foi ', 'montada ', 'com ', 'FOR']:
        a = a + x
    print(a)

    #início na posição 0, indo até 10 pulando de 2 em 2
    for x in range(0, 10, 2):
        print(f"Número RANGE 1: ",x)

    #indo até 2 começando na posição 10 (não vai mostrar nada), pulando de 1 em 1
    for x in range(10, 2):
        print(f"Número RANGE 2: ",x)

    #indo até 10 (começa com 0 e pula de 1 em 1)
    for x in range(10):
        print(f"Número RANGE 3: ",x)



if __name__ == '__main__':
    first_steps()