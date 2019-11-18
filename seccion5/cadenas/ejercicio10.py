# Ejercicio 10
#
# Introducir una cadena de caracteres e indicar si es un palíndromo.
# Una palabra palíndroma es aquella que se lee igual adelante que atrás.

cadena = input("Introduzca una cadena por teclado: ")
cadena = cadena.strip()

if cadena.lower() == cadena[::-1].lower():
    print("La cadena introducida: ", cadena, "SI es una palíndromo")
else:
    print("La cadena introducida: ", cadena, "NO es una palíndromo")
