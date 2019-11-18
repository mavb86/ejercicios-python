# Ejercicio 9
#
# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cadena = input("Introduzca una cadena por teclado: ")
cadena = cadena.strip()

subcadena = input("Introduzca una subcadena por teclado: ")
subcadena = subcadena.strip()

if cadena.find(subcadena) != -1:
    print("La subcadena: ", subcadena, " existe en la cadena: ", cadena)
else:
    print("La subcadena: ", subcadena, " NO existe en la cadena: ", cadena)
