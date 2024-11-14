# import datetime
# import time
from datetime import datetime

# hora = time.time()
# print(hora)


# fecha = datetime.datetime(2024, 11, 14)
# print(fecha)

fecha = datetime(2024, 11, 14)
fecha2 = datetime(2024, 12, 14)
ahora = datetime.now()

fechaStr = datetime.strptime("03-11-1987", "%d-%m-%Y")
# google: python 3 strptime directives

print(ahora.strftime("%Y.%m.%d"))
print(fecha > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)
