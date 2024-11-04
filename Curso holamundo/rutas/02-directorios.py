from pathlib import Path

path = Path("rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("Pipi")

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("01*.py")]
archivos = [p for p in path.glob("**/*.py")]  # incluye subcarpetas
archivos = [p for p in path.rglob("*.py")]  # tambien incluye r=recursivo
print(archivos)
