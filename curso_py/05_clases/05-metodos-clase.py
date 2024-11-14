class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad  # propiedad de la clase

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Tato", 4)


Perro.habla()
perro1 = Perro("Caco", 2)
perro2 = Perro("Pipi", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
