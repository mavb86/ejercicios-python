# Ejercicio 11
#
# El día juliano correspondiente a una fecha es un número entero que indica los días que
# han transcurrido desde el 1 de enero del año indicado.
# Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde.
#
# Para ello podemos hacer las siguientes subrutinas:
#
#     LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#
#     DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#
#     EsBisiesto: Recibe un año y nos dice si es bisiesto.
#
#     Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.


def leer_fecha():
    dia_sal = int(input("Dia: "))
    mes_sal = int(input("Mes: "))
    anio_sal = int(input("Año: "))
    return dia_sal, mes_sal, anio_sal


def dias_del_mes(mesp, aniop):
    if mesp in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mesp in [4, 6, 9, 11]:
        return 30
    elif mesp == 2:
        if bisiesto(aniop):
            return 29
        else:
            return 28


def bisiesto(aniop):
    return (aniop % 4 == 0 and not (aniop % 100 == 0)) or aniop % 400 == 0


def diajuliano(diap, mesp, aniop):
    diaj = 0
    for i in range(1, mesp):
        diaj = diaj + dias_del_mes(i, aniop)
    diaj = diaj + diap
    return diaj


dia, mes, anio = leer_fecha()
print("El día juliano es: ", diajuliano(dia, mes, anio))
