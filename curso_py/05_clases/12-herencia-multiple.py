class Animal:
    def comer(self):
        print("comiendo")


class Perro():
    def pasear(self):
        print("paseando")


class Gato(Perro, Animal):
    def programar(self):
        print("programando")


gato = Gato()
