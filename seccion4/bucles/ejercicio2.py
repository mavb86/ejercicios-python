# Ejercicio 2
#
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
# a demás de los intentos que te quedan (tienes 10 intentos para acertarlo).
# El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado),
# si se llega al limite de intentos te muestra el número que había generado.

import random

numero_aleatorio = random.randint(1, 100)
numero_usuario = int(input("Elija un número entre el 1 y el 100: "))
intentos = 10

while numero_usuario != numero_aleatorio and intentos > 1:
    intentos -= 1
    if numero_usuario > numero_aleatorio:
        print("El numero que has elegido es mayor que el aleatorio")
    else:
        print("El numero que has elegido es menor que el aleatorio")
    print("Le quedan ", intentos, " intentos")
    numero_usuario = int(input("Vuelva a elegir un número entre el 1 y el 100: "))

if numero_usuario == numero_aleatorio:
    print("Enhorabuena has acertado, el número aleatorio era: ", numero_aleatorio, " y lo has acertado en ",
          11 - intentos," intentos")
else:
    print("Lo sentimos pero no has acertado en ninguno de los 10 intentos, el numero secreto era: ", numero_aleatorio)
