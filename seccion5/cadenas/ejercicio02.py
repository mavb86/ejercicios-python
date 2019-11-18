# Ejercicio 2
#
# Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

cadena = input("Escriba una cadena: ")

subcadena = input("Escriba una subcadena de la cadena anterior y comprobaremos que comienze por ella: ")

if cadena.startswith(subcadena):
    print("La cadena comienza por ", subcadena)
else:
    print("La cadena no comienza por la subcadena que ha introducido")