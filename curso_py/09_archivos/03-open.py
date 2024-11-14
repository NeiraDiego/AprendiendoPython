from io import open

# escritura
# texto = "Hola mundo!"

# archivo = open(
#     "Programacion/Python/Curso holamundo/archivos/hola-mundo.txt",
#     "w"
# )
# archivo.write(texto)
# archivo.close()

# # lectura
# archivo = open(
#     "Programacion/Python/Curso holamundo/archivos/hola-mundo.txt",
#     "r"
# )
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# archivo = open(
#     "Programacion/Python/Curso holamundo/archivos/hola-mundo.txt",
#     "r"
# )
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with y seek
# with open(
#     "Programacion/Python/Curso holamundo/archivos/hola-mundo.txt",
#     "r",
#     encoding="utf-8"
# ) as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)


# with y seek
# archivo = open(
#     "Programacion/Python/Curso holamundo/archivos/hola-mundo.txt",
#     "a+",
#     encoding="utf-8"
# )
# archivo.write("\nChao mundo :(")

# lectura y escritura
with open(
    "Programacion/Python/Curso holamundo/archivos/hola-mundo.txt",
    "r+",
    encoding="utf-8"
) as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Diego"
    archivo.writelines(texto)
