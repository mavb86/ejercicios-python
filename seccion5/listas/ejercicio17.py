# Ejercicio 17
#
# Crear un programa que añada números a una lista hasta que introducimos un número negativo.
# A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados.
# Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

lista = []
lista_sin_duplicados = []

while True:
    num = int(input("Escriba un numero entero para añadir a la lista (negativo para terminar): "))
    if num < 0:
        break
    else:
        lista.append(num)

for num in lista:
    if num not in lista_sin_duplicados:
        lista_sin_duplicados.append(num)


for num in lista_sin_duplicados:
    print(num, " ", end="")
print()
