def no_space(texto):
    texto2 = ""
    for char in texto:
        if char != " ":
            texto2 += char
    return texto2


def reversar(texto):
    texto2 = ""
    for char in texto:
        texto2 = char + texto2
    return texto2


def es_palindromo(texto):
    texto = no_space(texto)
    textoalverres = reversar(texto)
    return texto.lower() == textoalverres.lower()
    # reversar los caracteres del string


print(es_palindromo("hola como estas"))
print(es_palindromo("Amo la paloma"))
print(es_palindromo("reconoCer"))
