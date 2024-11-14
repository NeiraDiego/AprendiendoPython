punto = { "x": 25, "y":50}
print(punto)
# print(punto["x"])
# print(punto["y"])

punto["z"] = 45
print(punto)

if "lala" in punto:
    print("enontré lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])

punto["x"] = 25

print(punto)

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id":1,"nombre":"Diego"},
    {"id":2,"nombre":"Adriana"},
    {"id":3,"nombre":"Martin"},
    {"id":4,"nombre":"Tata"},
]

for usuario in usuarios:
    print(usuario["nombre"])
