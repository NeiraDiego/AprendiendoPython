from abc import ABC


class Model():
    @property
    @classmethod
    def tabla(self):
        pass

    @classmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f"Guardando usuario")


usuario = Usuario()
Usuario.buscar_por_id(123)
