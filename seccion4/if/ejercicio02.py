#Ejercicio 2
# Algoritmo que pida un número y diga si es positivo, negativo o 0.

num = float(input("Indique un numero: "))

if num > 0:
    print("El número es positivo")
elif num == 0:
    print("El número es 0")
elif num <= 0:
    print("El número es negativo")
