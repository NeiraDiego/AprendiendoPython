# set significa grupo o conjunto
primer = {1, 2, 2, 3, 4}
# primer.add(6)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)

# print(primer | segundo) # es la union
# print(primer & segundo) # es la interseccion
# print(primer - segundo) # diferencia
# print(primer ^ segundo) # diferencia simetrica

# segundo[0], no se puede
if 5 in segundo:
    print("si esta el 5")
