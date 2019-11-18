# Ejercicio 5
#
# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono.
#
# El programa nos dará el siguiente menú:
#     Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y,
#     opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra,
#     debe permitir ingresar el teléfono correspondiente.
#
#     Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
#
#     Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#
#     Listar: Nos muestra todos los contactos de la agenda.
#
# Implementar el programa con un diccionario.

agenda = {}
while True:
    print("\n")
    print("1- Añadir/modificar")
    print("2- Buscar")
    print("3- Borrar")
    print("4- Listar")
    print("5- Salir")

    opcion = int(input("Teclea una opción:"))
    if opcion == 1:
        nombre = input("Nombre del contacto:")
        if nombre in agenda:
            print("{0} ya existe su número de teléfono es {1}".format(nombre, agenda[nombre]))
            opcion = input("Pulsa 's' para modificarlo. Otra tecla para continuar.")
            if opcion.lower() == "s":
                numero = input("Indique nuevo número de teléfono:")
                agenda[nombre] = numero
        else:
            numero = input("Indique el número de teléfono:")
            agenda[nombre] = numero
    elif opcion == 2:
        cadena = input("Nombre del contacto a buscar:")
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                print("El número de teléfono de {0} es el {1}".format(nombre, agenda[nombre]))
    elif opcion == 3:
        nombre = input("Nombre del contacto para borrar:")
        if nombre in agenda:
            opcion = input("Pulsa 's' si desea borrarlo. Otra tecla para continuar.")
            if opcion.lower() == "s":
                del agenda[nombre]
        else:
            print("No existe el contacto en la agenda")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre, "->", numero)
    elif opcion == 5:
        break
    else:
        print("La opción seleccionada es incorrecta")