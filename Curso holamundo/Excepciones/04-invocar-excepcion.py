class MiError(Exception):
    "este es mi error personalizado"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - código: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por cero", 805)
    return 5 / n


try:
    division()
except MiError as e:
    print(e)
