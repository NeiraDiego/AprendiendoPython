import sqlite3

with sqlite3.connect(
        "/home/diego/Programacion/Python/Curso holamundo/sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios 
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
