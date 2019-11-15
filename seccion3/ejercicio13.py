# Ejercicio 13
# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna
# función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?

import math

print("****************************")
print("* SECCION 3 - EJERCICIO 13 *")
print("****************************")

num = float(input("Escriba el número para calcular la raiz cuadrada y la raiz cúbica: "))

raiz_cuadrada = math.sqrt(num)
raiz_cubica = num ** (1 / 3)

print("El valor de la raíz cuadrada es: ", raiz_cuadrada)
print("El valor de la raíz cúbica es  : ", raiz_cubica)



