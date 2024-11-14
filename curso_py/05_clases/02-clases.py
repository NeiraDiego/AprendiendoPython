class Perro:
    # convension para nombres Pascal Case o Upper Camel Case
    def habla(self):  # no es funcion sino método
        print("Guau!")
       # print(self)


mi_perro = Perro()
# print(type(mi_perro))
# mi_perro.habla()
print(isinstance(mi_perro, Perro))
