numeros = [2, 5, 18, 1, 12]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

# usuarios = [
#     ["Diego", 4],
#     ["Adriana", 1],
#     ["Martin", 2]
# ]
# usuarios.sort()
# print(usuarios)

usuarios = [
    ["Diego", 4],
    ["Adriana", 1],
    ["Martin", 2]
]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)
