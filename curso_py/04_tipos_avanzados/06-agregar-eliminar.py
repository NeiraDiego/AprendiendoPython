mascotas = [
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Pelusa",
    "Chanchito feliz"]

mascotas.insert(1, "Diego")
mascotas.append("Martin")
mascotas.remove("Pulga")
mascotas.pop()  # remueve el ultimo elemento de la lista
mascotas.pop(1)
del mascotas[0]

# mascotas.clear()

print(mascotas)
