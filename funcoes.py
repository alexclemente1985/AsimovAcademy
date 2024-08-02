def funcoes():
    def diga_ola(nome):
        print(f"Ooolá {nome}!")

    def gerador_numeros_impares(x):
        return [i for i in range(x) if i % 2 == 1]

    diga_ola("Joelma")
    diga_ola("Joselma")
    diga_ola("Moema")

    lista_impares = gerador_numeros_impares(11)
    print(f"Lista de ímpares: {lista_impares}")

    def funcao_vazia():
        pass

    funcao_vazia()

    def elevar_quadrado(x):
        return x ** 2

    print(elevar_quadrado(10))

    a = lambda base_pot: base_pot ** 2

    print("Função lambda da potência ao quadrado: ", a(5))
