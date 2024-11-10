from pathlib import Path

archivo = Path(
    "Programacion/Python/Curso holamundo/archivos/archivo-prueba.txt"
)
texto = archivo.read_text("utf-8").split("\n")
# texto.insert(0, "Titulo: Lorem Ipsum")
archivo.write_text("\n".join(texto), "utf-8")
