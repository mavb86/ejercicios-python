# Ejercicio 3
#
# Vamos a crear un programa en python donde vamos a declarar un diccionario
# para guardar los precios de las distintas frutas.
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta
# a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error.
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

precios = {"naranja": 2, "pera": 3, "manzana": 1, "melocoton": 5, "melon": 7}

while True:
    fruta = input("Indique la fruta que se ha vendido: ")
    if fruta.lower() not in precios:
        print("ERROR: La fruta que ha indicado no existe en el sistema")
    else:
        cantidad = int(input("Indique la cantidad de {0} que se ha vendido: ".format(fruta)))
        print("El precio de la fruta es de {0}".format(cantidad * precios[fruta]))
    while True:
        opcion = input("¿Quieres vender otra fruta (s/n): ")
        if opcion.lower() != "s" and opcion.lower() != "n":
            print("ERROR: Solo puede seleccionar como opción (s/n)")
        else:
            break
    if opcion.lower() == "n":
        break
