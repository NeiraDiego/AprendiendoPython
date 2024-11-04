class Perro:
    def __init__(self, nombre, edad):  # metodo mágico porque no lo necesitas llamar
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def __del__(self):
        print(f"Chao Perro : {self.nombre}")

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Caco", 6)
del perro
