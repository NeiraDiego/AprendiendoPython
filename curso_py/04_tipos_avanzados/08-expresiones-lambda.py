usuarios = [
    ["Diego", 4],
    ["Adriana", 1],
    ["Martin", 2]
]


# def ordena(elemento):
#     return elemento[1]
# lambda parametros:valorRetorno

usuarios.sort(key=lambda elemento: elemento[1])
print(usuarios)
