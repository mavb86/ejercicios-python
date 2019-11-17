# Ejercicio 4
#
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

num_introducir = int(input("Indique cuantos números desea introducir: "))

i = 1
menor = 0
igual = 0
mayor = 0

while i <= num_introducir:
    print("*** Número ", i, " ***")
    num = int(input("Introduzca el número que desea ingresar: "))
    if num < 0:
        menor += 1
    elif num == 0:
        igual += 1
    elif num > 0:
        mayor += 1
    i += 1

print("Números introducidos menores que 0: ", menor)
print("Números introducidos igual a 0: ", igual)
print("Números introducidos mayores que 0: ", mayor)
