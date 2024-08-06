def texto_escolha(operador):
    print(f">>> {operador} escolhida.")

def info_escolha():
    continua_loop = True
    while continua_loop:
        valor = input("Escolha a operação que deseja realizar: \n")

        match (valor):
            case "0":
                texto_escolha("+")
                return "+"
            case "1":
                texto_escolha("-")
                return "-"
            case "2":
                texto_escolha("*")
                return "*"
            case "3":
                texto_escolha("/")
                return "/"
            case "4":
                texto_escolha("** (exp)")
                return "**"
            case _:
                print("Valor inválido... escolha novamente")
                continue


