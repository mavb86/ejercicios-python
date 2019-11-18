# Ejercicio 5
#
# Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

iniciales = ""
posicion = 0

while True:
    cadena = input("Introduzca nombres y apellidos: ")
    cadena = cadena.strip()
    if cadena.count(" ") >= 1:
        break
    else:
        print("ERROR: No ha introducido una cadena con espacios, por lo tanto no ha introducillo apellidos")

# Busco los espacios
posicion = cadena.find(" ", posicion)
iniciales = cadena[0]
while posicion != -1:
    # No tengo en cuenta los posibles espacios que haya entre las palabras
    while cadena[posicion + 1] == " ":
        posicion = posicion + 1
    iniciales = iniciales + cadena[posicion + 1]
    posicion = cadena.find(" ", posicion + 1)

print("Iniciales:", iniciales.upper())
