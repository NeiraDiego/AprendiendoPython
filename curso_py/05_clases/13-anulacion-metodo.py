# Method override
class Ave:
    def __init__(self):
        self.vuela = True

    def volador(self):
        print("vuela ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = True

    def volador(self):
        super().volador()
        print("vuela pato")


pato = Pato()
pato.volador()
print(pato.vuela, pato.nada)
