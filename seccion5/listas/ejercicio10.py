# Ejercicio 10
#
# Diseñar el algoritmo correspondiente a un programa, que:
#
#     Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#
#     Carga la tabla con valores numéricos enteros.
#
#   Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

tabla = []

for indice_fila in range(1, 6):
    fila = []
    for indice_columna in range(1, 6):
        fila.append(int(input("Introduzca el valor de la fila {0} y la columna {1}: ".format(indice_fila,
                                                                                             indice_columna))))
        tabla.append(fila)

# Suma las filas
indice_fila = 1
for fila in tabla:
    print("La suma de los elemento de la fila {0} es {1}".format(indice_fila, sum(fila)))
    indice_fila += 1

# Suma las columnas
for indice_columna in range(1, 6):
    suma = 0
    for fila in tabla:
        suma = suma + fila[indice_columna - 1]
    print("La suma de los elemento de la columna {0} es {1}".format(indice_columna, suma))

