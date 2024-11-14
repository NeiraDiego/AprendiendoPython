import sqlite3

with sqlite3.connect(
        "/home/diego/Programacion/Python/Curso holamundo/sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Chanchito feliz"),
        (3, "Chanchito triste")
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )
