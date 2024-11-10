import csv
import os


# escribir
# with open(
#     "Programacion/Python/Curso holamundo/archivos/archivo.csv",
#     "w",
#     encoding="utf-8"
# ) as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow(["1000", "1", "Este es un twit"])
#     writer.writerow(["1001", "2", "otro twit!"])

# leer
# with open(
#     "Programacion/Python/Curso holamundo/archivos/archivo.csv",
#     encoding="utf-8"
# ) as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# actualizar csv
with open(
    "Programacion/Python/Curso holamundo/archivos/archivo.csv",
    encoding="utf-8"
) as r, open(
    "Programacion/Python/Curso holamundo/archivos/archivo_temp.csv",
    "w",
    encoding="utf-8"
) as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("Programacion/Python/Curso holamundo/archivos/archivo.csv")
    os.rename(
        "Programacion/Python/Curso holamundo/archivos/archivo_temp.csv",
        "Programacion/Python/Curso holamundo/archivos/archivo.csv"
    )
