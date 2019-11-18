# Ejercicio 8
#
# Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

cadena = input("Introduzca una cadena por teclado: ")
cadena = cadena.strip()

cadena = cadena.swapcase()

print(cadena)
