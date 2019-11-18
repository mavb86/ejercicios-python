# Ejercicio 7
#
# Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cadena = input("Introduzca una cadena: ")
cadena = cadena.strip()

while True:
    caracter1 = input("Introduzca un caracter a buscar: ")
    caracter1 = caracter1.strip()
    if len(caracter1) == 1:
        break
    else:
        print("ERROR: No ha introducido un único caracter")

while True:
    caracter2 = input("Introduzca un caracter a sustituir: ")
    caracter2 = caracter2.strip()
    if len(caracter2) == 1:
        break
    else:
        print("ERROR: No ha introducido un único caracter")

cadena = cadena.replace(caracter1, caracter2)

print(cadena)
