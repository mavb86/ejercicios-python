# Ejercicio 9
#
# Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:
#
#     Se divide el número mayor entre el menor.
#
#     Si la división es exacta, el divisor es el MCD.
#
#     Si la división no es exacta, dividimos el divisor entre el resto obtenido
#     y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
#
# Crea un programa principal que lea dos números enteros y muestre el MCD.


def mcd(num1, num2):
    resto = num1 % num2
    if resto == 0:
        return num2
    else:
        return mcd(num2, resto)


while True:
    num_men = int(input("Introduce un número menor: "))
    num_may = int(input("Introduce un número mayor al anterior: "))
    if num_men > num_may:
        print("ERROR: El número menor debe ser menor al mayor")
    else:
        break

print("MCD: ", mcd(num_may, num_men))
