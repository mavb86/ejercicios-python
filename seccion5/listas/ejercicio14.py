# Ejercicio 14
#
# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales.
#
# Informar:
#     Las cantidades totales de cada articulo.
#     La cantidad de artículos en la sucursal 2.
#     La cantidad del articulo 3 en la sucursal 1.
#     La recaudación total de cada sucursal.
#     La recaudación total de la empresa.
#     La sucursal de mayor recaudación.

precios = []
cantidades = []

num_articulos = 5
num_sucursales = 4

# Leer precios
for indice_art in range(0, num_articulos):
    precios.append(float(input("Indique el precio del artículo {0}: ".format(indice_art + 1))))

# Leer cantidades
for indice_sucursal in range(0,num_sucursales):
    cant_articulos = []
    for indice_art in range(0, num_articulos):
        cant_articulos.append(int(input('Ingrese Cant. de Articulo {0}, en sucursal {1}:'
                                  .format(indice_art + 1, indice_sucursal + 1))))
    cantidades.append(cant_articulos)

# Las cantidades totales de cada articulo.
for indice_articulos in range(0, num_articulos):
    suma = 0
    for cant_sucursal in cantidades:
        suma = suma + cant_sucursal[indice_articulos]
    print('Total articulo {0}: {1}'.format(indice_articulos + 1, suma))

# La cantidad de artículos en la sucursal 2.
print('Total Sucursal 2: {0}'.format(sum(cantidades[1])))

# La cantidad del articulo 3 en la sucursal 1.
print('Sucursal 1, Articulo 3: {0}'.format(cantidades[0][2]))

# La recaudación total de cada sucursal.
total_por_sucursal = []
for precio, cant_sucursal in zip(precios, cantidades):
    total_por_sucursal.append(sum(cant_sucursal) * precio)

# La recaudación total de cada sucursal.
mayorrec = max(total_por_sucursal)
indice_sucursal = 1
for cant_sucursal in cantidades:
    print('Recaudaciones Sucursal {0}: {1}'.format(indice_sucursal,sum(cant_sucursal)))
    indice_sucursal += 1

# La sucursal de mayor recaudación.
indice_sucursal = 1
for cant_sucursal in total_por_sucursal:
    if cant_sucursal == mayorrec: break
    indice_sucursal += 1

print('Recaudación total de la empresa: {0}'.format(sum(total_por_sucursal)))
print('Sucursal de Mayor Recaudación: {0}'.format(indice_sucursal))