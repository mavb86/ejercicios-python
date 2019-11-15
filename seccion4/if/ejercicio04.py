# Ejercicio 4
# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
# o un mensaje de aviso en caso contrario.

num1 = float(input("Indique el primer número: "))
num2 = float(input("Indique el segundo número: "))

if num2 == 0:
    print("El segundo numero no puede ser 0")
else:
    print("El resultado de la división de ambos numeros es: ", num1 / num2)
