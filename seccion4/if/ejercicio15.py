# Ejercicio 15
# El director de una escuela está organizando un viaje de estudios,
# y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
# La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros;
# de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30,
# el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses
# y lo que debe pagar cada alumno por el viaje.

alumnos = int(input("Introduzca el número de alumnos: "))

precio_x_alumno = 0

if alumnos >= 100:
    precio_x_alumno = 65
elif 50 <= alumnos <= 99:
    precio_x_alumno = 70
elif 30 <= alumnos <= 49:
    precio_x_alumno = 95
elif alumnos < 30:
    precio_x_alumno = 4000 / alumnos

if alumnos > 0:
    precio_autobus = alumnos * precio_x_alumno
    print("El precio por alumno es de: ", precio_x_alumno)
    print("El precio del autobus es de: ", precio_autobus)
else:
    print("El numero de alumnos debe de ser un valor positivo")


