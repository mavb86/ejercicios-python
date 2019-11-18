# Ejercicio 3
#
# Pide una cadena y un carácter por teclado (valida que sea un carácter) y
# muestra cuantas veces aparece el carácter en la cadena.

cadena = input("Introduzca una cadena: ")

while True:
    caracter_buscar = input("Introduzca un caracter: ")
    if len(caracter_buscar) == 1:
        break
    else:
        print("ERROR: Solo puede introducir un caracter")

print("En la cadena que ha escrito ", cadena, " aparecen", cadena.count(caracter_buscar),
      "veces el carácter", caracter_buscar)

