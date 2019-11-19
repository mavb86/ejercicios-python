# Ejercicio 6
#
# Diseñar una función que calcule el área y el perímetro de una circunferencia.
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

import math


def area_perimetro(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

radio = float(input("Introduzca el radio de la circunferencia: "))

area, perimetro = area_perimetro(radio)
print("El area de la circunferencia es ", area)
print("El area de la circunferencia es ", perimetro)
