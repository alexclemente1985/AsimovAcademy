def display_operacao(valor_1, valor_2, operador, resultado):
    print(f"{valor_1} {operador} {valor_2} = {resultado}")

def operacao(valor_1, valor_2, operador):
    resultado = 0
    match(operador):
        case "+":
            resultado = valor_1 + valor_2
        case "-":
            resultado = valor_1 - valor_2
        case "*":
            resultado = valor_1 * valor_2
        case "/":
            resultado = valor_1 / valor_2
        case "**":
            resultado = valor_1 ** valor_2

    display_operacao(valor_1, valor_2, operador, resultado)


