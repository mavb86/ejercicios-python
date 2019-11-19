# Ejercicio 10
#
# Escribir dos funciones que permitan calcular:
#
#     La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#
#     La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#
# Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos,
# convertir a horas,minutos y segundos o salir del programa.

def segundos_a_hms(seg):
    # Horas = Divisíón entera de los segundos entre 3600
    h = seg // 3600
    # Decremento los segundos que me quedan por convertir
    seg = seg - h * 3600
    # Minutos = División entera de los segundos entre 60
    m = seg // 60
    # Decremento los segundos que me quedan por convertir
    seg = seg - m * 60
    # Lo que me quedan corresponden a los segundos
    s = seg
    return h, m, s


def hms_a_segundos(h, m, s):
    return h * 3600 + m * 60 + s


while True:
    print("1.- Convertir a segundos")
    print("2.- Convertir a horas, minutos y segundos")
    print("3.- Salir")
    opcion = int(input())
    if opcion == 1:
        horas = int(input("Horas:"))
        minutos = int(input("Minutos:"))
        segundos = int(input("Segundos:"))
        print("Corresponde a", hms_a_segundos(horas, minutos, segundos), "segundos.")
    elif opcion == 2:
        segundos = int(input("Segundos:"))
        horas, minutos, segundos = segundos_a_hms(segundos)
        print("Corresponde a ", horas, ":", minutos, ":", segundos)
    elif opcion == 3:
        break
    else:
        print("Opción incorrecta")
