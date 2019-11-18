# Ejercicio 2
#
# Escribe un programa que lea una cadena y devuelva un diccionario
# con la cantidad de apariciones de cada carácter en la cadena.

cadena = input("Escriba una cadena: ")
diccionario = {}

for caracter in cadena:
    if caracter in diccionario:
        diccionario[caracter] += 1
    else:
        diccionario[caracter] = 1

for campo, valor in diccionario.items():
    print(campo, "->", valor)
