# Ejercicio 1
#
# Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla
# (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto).
# Además subraya el mensaje utilizando el carácter =.


def centrartexto(cadena):
    print(" " * int(40 - (len(cadena) / 2)), cadena)
    print(" " * int(40 - (len(cadena) / 2)), "=" * len(cadena))


prueba = "Voy a centrar este texto a traves de una funcion de Python"
centrartexto(prueba)
