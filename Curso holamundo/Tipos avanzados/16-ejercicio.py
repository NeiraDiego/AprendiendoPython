from pprint import pprint
# 1 Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes
# comprension de lista
# string = list(filter(lambda caracter: caracter != " ", palabra))
# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string
# veces_letra = {}
# for letra in string:
#     veces_letra[letra] = 1
# print(veces_letra)
# 3 Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que ocntiene tuplas [("a",3),("b",2)...]
# 4. de un listado de tuplas, devolver las
# que tengan el mayor valor
# 5 Crear un mensaje que diga:
# LOs caractores que mas ser repiten con 4 rep son
# - C
# - D
# 6 Juntar la solucion de los ejercicios anteriores
# para encontrar los caracteres que más se repiten
# en un string


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dicta):
    return sorted(
        dicta.items(),
        key=lambda key: key[1],
        reverse=True,
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    mensaje = "Los que más se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


string = " soy el Diego "
sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)

print(mensaje)