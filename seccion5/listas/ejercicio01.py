# Ejercicio 1
#
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
# posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

lista = []

for i in range(1, 11):
    lista.append(random.randint(1, 10))

for numero in lista:
    print("Numero: ", numero, "Cuadrado: ", numero * numero, "Cubo: ", numero * numero * numero)

