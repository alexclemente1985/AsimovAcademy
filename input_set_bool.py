def input_set_bool():

    a = input("Insira o valor da variável 'a': ")

    print(f"Variável a: {a}")

    b = "123"
    print(f"Conversão de variáveis: {int(b)} | {float(b)}")

    x = set()
    print("Valor de x: ", x)

    x.add(123)
    print("Valor novo de x: ", x)

    x.add(321)
    x.add(3)

    x.add(3)
    print("Valor de x com adições: ", x)

    l = [1,2,3,4,5,6,7,8,9]

    l1 = set(l)
    print("Valor de l1: ", l1)

    z = x.union(l1)

    y = x.intersection(l1)

    print("X com union com l1: ",z)
    print("x interseção com l1: ",y)

    a = True
    b = False


if __name__ == '__main__':
    input_set_bool()