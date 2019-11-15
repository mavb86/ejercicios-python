# Ejercicio 9
#
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

num1 = float(input("Introduzca el numero 1: "))
num2 = float(input("Introduzca el numero 2: "))
num3 = float(input("Introduzca el numero 3: "))

if num1 >= num2 and num1 >= num3:
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)

if num2 >= num1 and num2 >= num3:
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)

if num3 >= num1 and num3 >= num2:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)
