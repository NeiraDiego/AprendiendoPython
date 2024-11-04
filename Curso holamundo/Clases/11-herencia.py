class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")

    # def comer(self):
    #     print("comiendo")


class Gato(Perro):
    # def comer(self):
    #     print("comiendo")

    def prigramar(self):
        print("programando")


gato = Gato()
perro = Perro()
