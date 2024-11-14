n1 = ""

print("""
Bienvenido al programa de calculadora,
puedes usar las operaciones suma, resta, mult, o div
""")
while True:
    if not n1:
        n1 = input("Ingrese un numero: ")
        if n1.lower() == "salir":
            break
        n1 = int(n1)
    op = input(
        "Ingrese una operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese otro numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op == "suma":
        n1 = n1 + n2
    if op == "resta":
        n1 = n1 - n2
    if op == "mult":
        n1 = n1 * n2
    if op == "div":
        n1 = n1 / n2
    print(
        f"""el resultado es {n1}
quiere realizar otra operacion? si no, escriba salir""")
print("ok, adios")
