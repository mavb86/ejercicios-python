# Ejercicio 5
#
# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario,
# el programa termina cuando se introduce un espacio.

continuar = True

while continuar:
    cadena = input("Introduzca una letra y averiguaremos si es una vocal o no "
                   "(para salir del programa introduzca un espacio): ")
    if cadena.upper() == "A" or cadena.upper() == "E" or cadena.upper() == "I" or cadena.upper() == "O" or \
       cadena.upper() == "U":
        print("VOCAL")
    else:
        if cadena == " " or cadena == "":
            continuar = False
            print("Salida del programa")
        else:
            print("NO VOCAL")
