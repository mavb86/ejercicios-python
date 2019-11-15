# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#
#     Si se cumple Pitágoras entonces es triángulo rectángulo
#
#     Si sólo dos lados del triángulo son iguales entonces es isósceles.
#
#     Si los 3 lados son iguales entonces es equilátero.
#
#     Si no se cumple ninguna de las condiciones anteriores, es escaleno.

a = float(input("Indique el lado A del triangulo: "))
b = float(input("Indique el lado B del triangulo: "))
c = float(input("Indique el lado C del triangulo: "))

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("El triangulo es rectángulo")

if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
    print("El triangulo es isosceles")
else:
    if a == b and a == c:
        print("El triangulo es equilatero")
    else:
        print("El triangulo es escaleno")
