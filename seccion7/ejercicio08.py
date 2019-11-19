# Ejercicio 8
#
# Crear una función recursiva que permita calcular el factorial de un número.
# Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


numero = int(input("Indique un número para calcular el factorial: "))
print("El factorial del número {0} es ".format(factorial(numero)))

