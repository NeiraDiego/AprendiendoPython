# # import Correa

# # class Perro:
# #     def __init__(self):
# #         self.correa = Correa()


# class Perro:
#     def __init__(self, Correa):
#         self.correa = Correa()

# import usuario


# def guardar():
#     usuario.guardar()


# def guardar(entidad):
#     entidad.guardar()

from pathlib import Path
# from db import db
# import graphql
# import api

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",  # db
    "api": "esta es la api",  # api
    "graphql": "esto es graphql"  # graphql
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("el paquete no tiene funcion init")


list(map(load, paths))
