#Dados los catetos de un triangulo rectangulo, calcular la hipotenusa
import math

cateto = float(input("Indique el valor del cateto del triangulo rectangulo:"))
hipotenusa = math.sqrt(cateto**2 + cateto**2)

print("El valor de la hipotenusa es: ", hipotenusa)

