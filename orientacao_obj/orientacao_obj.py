from classes.dog import Dog


class Exemplo:
    pass

def orientacao_obj():


    exemplo = Exemplo()
    print(type(exemplo))

    dog = Dog(nome="Rasputin", raca="Dalmata")
    dog.envelhecer()
    print(dog.idade)
    print(dog.raca)

    dog.correr()
    print(dog)





orientacao_obj()
