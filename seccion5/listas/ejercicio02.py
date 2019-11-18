# Ejercicio 2
#
# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado.
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

lista1 = []
lista2 = []

for i in range(1, 6):
    while True:
        caracter = input("Introduzca el caracter {0}: ".format(i))
        if len(caracter) != 1:
            print("ERROR: No ha escrito un único caracter")
        else:
            lista1.append(caracter)
            break

# Copio la lista1 en la lista2 en orden inverso
lista2 = lista1[::-1]

for i in lista2:
    print(i)
