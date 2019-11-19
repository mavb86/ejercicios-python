# Ejercicio 3
#
# Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
# Crear un programa principal, que utilizando la función anterior,
# vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media.
# El programa pedirá el número de días que se van a introducir.


def temperatura_media(temp1, temp2):
    return temp1 + temp2 / 2


dias = int(input("Introduce el número de días en los que vas a registrar la temperatura: "))

for dia in range(dias):
    while True:
        temp_min = int(input("Introduce la temperartura mímina para el día {0}: ".format(dia + 1)))
        temp_max = int(input("Introduce la temperartura mímina para el día {0}: ".format(dia + 1)))
        if temp_min <= temp_max:
            break
        else:
            print("ERROR: La temperatura mímina no puede ser mayor que la maxima o vicevera, vuelva a insertarlas")
    print("La temperatura media del dia {0} es de {1} grados".format(dia + 1, temperatura_media(temp_min, temp_max)))
