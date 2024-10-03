from pathlib import Path

from classes.circle import Circle

classes_path = Path.joinpath(Path.cwd(),"classes")

from classes.dog import Dog


class Exemplo:
    pass

def orientacao_obj():


    exemplo = Exemplo()
    print(type(exemplo))

    dog = Dog("Dálmata")
    print(type(dog))
    dog.envelhecer()
    print(dog.idade)
    print(dog.raca)

    circle = Circle()



orientacao_obj()
