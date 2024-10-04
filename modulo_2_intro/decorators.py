def decorators():
    def decorador_maiusculo(function):
        def wrapper():
            func = function()
            cria_maiusculo = func.upper()
            return cria_maiusculo
        return wrapper

    def diga_oi():
        return "amigo estoy aqui"

    #Método 1: instanciamento do método decorador com a função desejada
    funcao_decorada = decorador_maiusculo(diga_oi)
    print(funcao_decorada())

    #Método 2: uso de decorator
    @decorador_maiusculo
    def diga_oi_2():
        return diga_oi()+' via decorator'

    print(diga_oi_2())

decorators()