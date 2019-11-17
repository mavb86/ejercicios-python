# Ejercicio 9
#
# Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente),
# saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = int(input("Introduzca la base para calcular la potencia: "))

while True:
    exponente = int(input("Introduzca exponente para calcular la potencia: "))
    if exponente < 0:
        print("ERROR: El exponente debe ser positivo")
    else:
        break

potencia = 1
for i in range(1, exponente + 1):
    potencia = potencia * base

print("El resultado de la potencia es: ", potencia)
