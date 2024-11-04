class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad  # propiedad de la clase

    def habla(self):
        print(f"{self.nombre} dice: Guau!, tengo {self.edad}")
# propiedad (en programacion orientada a objeto) -> atributo (python)


Perro.patas = 3
mi_perro = Perro("Caco", 2)
mi_perro.patas = 5
mi_perro2 = Perro("Felipe", 1)
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
