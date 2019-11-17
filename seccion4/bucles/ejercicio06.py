# Ejercicio 6
#
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

num1 = int(input("Escriba el número 1: "))
num2 = int(input("Escriba el número 2: "))

for num in range(num1, num2 + 1):
    if num != 0:
        if num % 2 == 0:
            print(num)
