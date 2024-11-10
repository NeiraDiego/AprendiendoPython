import json
from pathlib import Path

# escribir json
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"}
# ]

# data = json.dumps(productos)
# Path("Programacion/Python/Curso holamundo/archivos/productos.json").write_text(data)

# leer json
data = Path(
    "Programacion/Python/Curso holamundo/archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)

# modificar jsonPath(
productos[0]["name"] = "Diego"
Path("Programacion/Python/Curso holamundo/archivos/productos.json").write_text(
    json.dumps(productos), encoding="utf-8")
