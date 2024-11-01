usuarios = [
    ["Diego", 4],
    ["Adriana", 1],
    ["Martin", 2]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)


# lista = [expresion for item in items]

# map: separa una lista solo con los usuarios
# nombres = [usuario[0] for usuario in usuarios]

# filter: filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 1]

# nombres = list(map(lambda usuario: usuario[0], usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[1] > 1, usuarios))

print(menosUsuarios)
