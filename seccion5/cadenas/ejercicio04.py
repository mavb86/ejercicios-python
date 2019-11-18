# Ejercicio 4
#
# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
# realiza un programa que cuente cuantas palabras tiene.

cont = 0
posicion = 0

while True:
    cadena = input("Introduzca una frase (cadena con espacios): ")
    cadena = cadena.strip()
    if cadena.count(" ") >= 1:
        break
    else:
        print("ERROR: No ha introducido una cadena con espacios")

# Busco los espacios
posicion = cadena.find(" ", posicion)

while posicion != -1:
    cont = cont + 1
    # No tengo en cuenta los posibles espacios que haya entre las palabras
    while cadena[posicion + 1] == " ":
        posicion = posicion + 1
    posicion = cadena.find(" ", posicion + 1)
print("La frase tiene", cont + 1, "palabras.")
