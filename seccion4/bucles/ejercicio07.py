# Ejercicio 7
#
# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

tabla = int(input("Introduzca la tabla de multiplicar que quiere representar: "))

for i in range(1, 11):
    print(tabla, " x ", i, " = ", tabla * i)
