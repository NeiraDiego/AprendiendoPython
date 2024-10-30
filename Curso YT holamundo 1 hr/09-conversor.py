temperatura = int(input("Ingrese temperatura a convertir:"))

escala = input("Es Fahrenheit(F) o Celsius(C)?:").lower()

if escala == "c":
    print("La temperatura es: ",(temperatura*1.8)+32,"F")
elif escala == "f":
    print("La temperatura es: ",(temperatura-32)/1.8,"C")
else:
    print("escala incorrecta")