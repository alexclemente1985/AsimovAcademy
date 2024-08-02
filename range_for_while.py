def range_for_while():
    x = range(0,10,1)
    y = range(0,10)
    z = list(x)

    print(f"Range de valores: {x}, {y}, {z}")

    for i in x:
        print(f"Valor da lista: {i}")

    for i in "Alexandre":
        print("Letra: ", i)

    b = 0
    while b < 10:
        if(b % 2 == 0):
            b += 1
            continue
        print(f"O valor de b é : {b}")
        b += 1
    else:
        print("Loop while concluído!")