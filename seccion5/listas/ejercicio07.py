# Ejercicio 7
#
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno,
# pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

lista1 = []
lista2 = []
lista3 = []

for i in range(1, 6):
    lista1.append(int(input("Para la lista 1, introduzca el numero {0}: ".format(i))))
    lista2.append(int(input("Para la lista 2, introduzca el numero {0}: ".format(i))))

for i in range(0, 5):
    lista3.append(lista1[i] + lista2[i])

print("La suma de los valores de las dos listas es:")
for numero in lista3:
    print(numero, " ", end="")

