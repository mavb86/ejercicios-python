# Ejercicio 11
#
# Escribe un programa que diga si un número introducido por teclado es o no primo.
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

es_primo = True

num = int(input("Introduce el número para comprobar si es primo: "))
for i in range(2,num):
    if num % i == 0:
        es_primo = False

if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")
