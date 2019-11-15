# Ejercicio 17
#
# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre
# por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
#
#     Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#
#     Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje:
#     “ERROR: número incorrecto.”.
#
# Ejemplo:
#
#     Introduzca número del dado: 5
#     En la cara opuesta está el "dos".

dado = int(input("Introduzca el número del dado: "))

if 1 > dado > 6:
    print("ERROR: número incorrecto")
else:
    opuesto = ""
    if dado == 1:
        opuesto = "seis"
    elif dado == 2:
        opuesto = "cinco"
    elif dado == 3:
        opuesto = "cuatro"
    elif dado == 4:
        opuesto = "tres"
    elif dado == 5:
        opuesto = "dos"
    elif dado == 6:
        opuesto = "uno"
    print("El lado opuesto es: ", opuesto)
