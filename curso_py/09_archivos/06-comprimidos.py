from pathlib import Path
from zipfile import ZipFile

# with ZipFile("Programacion/Python/Curso holamundo/archivos/comprimidos.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         if string(path) != "Programacion/Python/Curso holamundo/archivos/comprimidos.zip":
#             zip.write(path)

# with ZipFile("Programacion/Python/Curso holamundo/archivos/comprimidos.zip") as zip:
#     # print(zip.namelist())
#     info = zip.getinfo(
#         "Programacion/Python/Curso holamundo/archivos/06-comprimidos.py")
#     print(
#         info.file_size,
#         info.compress_size,
#     )
#     zip.extractall("Programacion/descomprimidos")
