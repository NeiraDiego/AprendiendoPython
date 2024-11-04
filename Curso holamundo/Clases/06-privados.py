class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    def get_nombre(self):
        return self.__nombre

    @classmethod
    def factory(cls):
        return cls("Tato", 4)


perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())
print(perro1.__dict__)
