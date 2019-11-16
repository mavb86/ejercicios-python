# Ejercicio 3
# Algoritmo que pida números hasta que se introduzca un cero.
# Debe imprimir la suma y la media de todos los números introducidos.

num = int(input("Escriba un número (0 para salir): "))

suma = 0
num_insertados = 0

while num != 0:
    suma += num
    num_insertados += 1
    num = int(input("Vuelva a escribir un numero (0 para salir): "))

if num_insertados == 0:
    print("No ha insertado ningun número")
else:
    print("La suma de los números insertados es: ", suma)
    print("La media de los números insertados es: ", suma / num_insertados)




