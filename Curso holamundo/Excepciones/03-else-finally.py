try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:
    print("Ocurrió un error")
else:
    print("No ocurrió ningun error")
finally:
    print("se ejecuta siempre")
