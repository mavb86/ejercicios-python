# Ejercicio 5
#
# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.


def calcular_maxmin(lista):
    return max(lista), min(lista)


numeros = []

while True:
        try:
            num = int(input("Escriba algún número entero (escriba -999 para salir): "))
            if num == -999:
                break
            else:
                numeros.append(num)
        except ValueError:
                print("ERROR: Solo se permiten números enteros")

maximo, minimo = calcular_maxmin(numeros)

print("El valor máximo es: ", maximo)
print("El valor mínimo es: ", minimo)
