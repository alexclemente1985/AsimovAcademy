def condicionais():
    a = 1 > 2 > 3
    b = 1 > 2 and 2 < 3
    c = 1 > 2 or 2 < 3

    print("Condicional em cadeia: ", a, b, c)

    temp = 30
    if temp > 30:
        print("Calor")
    elif temp > 24 and temp <= 30:
        print("Clima fresco")
    else:
        print("Frio")

