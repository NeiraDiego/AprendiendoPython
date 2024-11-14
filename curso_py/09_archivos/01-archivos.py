from pathlib import Path
from time import ctime

archivo = Path(
    "Programacion/Python/Curso holamundo/archivos/archivo-prueba.txt",
)

print(archivo.stat())
print("acceso: ", ctime(archivo.stat().st_atime))
print("creación: ", ctime(archivo.stat().st_ctime))
print("modificación: ", ctime(archivo.stat().st_mtime))
