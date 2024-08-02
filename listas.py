def listas():
    lista = [1, 2, 3]

    print("Lista: {a}".format(a=lista))
    print("Tipo da lista: ", type(lista))
    print("lista[1:-1]: ", lista[1:-1])

    lista_teste = [1,2,"hello",lista]

    print("lista[3][1:]", lista_teste[3][1:])
    print("lista[2].upper(): ", lista_teste[2].upper())

    print("---Operações em lista---")
    print("duplicar lista: ", lista_teste * 2)
    lista_teste.append(10)
    print("adição de elemento no final: ", lista_teste)
    lista_teste.pop()
    print("remoção do último elemento da lista: ", lista_teste)
    print("ordenação de listas")
    l = ["a", "u", "z", "b"]
    print("lista original: ", l)
    l.sort()
    print("lista ordenada: ", l)
    l.reverse()
    print("lista invertida: ", l)

    print("lista de listas")
    l_listas = [l, lista, lista_teste]
    print(l_listas)
    return


if __name__ == '__main__':
    listas()
