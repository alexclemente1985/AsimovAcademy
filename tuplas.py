def tuplas():
    # Uma vez criadas elas não são alteráveis (diferente das listas)
    t = (1,2,3)

    print(t[1])
    print(t[:-1])

    a,b,c = t

    print(f"Desmembramento de tuplas: {a}, {b}, {c}")

if __name__ == '__main__':
    tuplas()
