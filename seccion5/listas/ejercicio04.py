# Ejercicio 4
#
# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo.
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

lista = []

while True:
    num = int(input("Introduzca un número (número negativo para salir): "))
    if num < 0:
        break
    else:
        lista.append(num)

for numero in lista:
    print(numero, " ", end="")
