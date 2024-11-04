class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad  # propiedad de la clase

    def habla(self):
        print(f"{self.nombre} dice: Guau!, tengo {self.edad}")


mi_perro = Perro("Caco", 2)
mi_perro2 = Perro("Pipi", 3)
mi_perro.habla()
