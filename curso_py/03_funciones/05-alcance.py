saludo = "Hola Global"


def saludar():
    global saludo
    saludo = "Hola Mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


saludar()
print(saludo)
saludaChanchito()
