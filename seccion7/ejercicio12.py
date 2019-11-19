# Ejercicio 12
#
# Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha.
# De tal forma que al leer una fecha se asegura que es válida.ç


def validar_fecha(diap, mesp, aniop):
    if diap < 1 or diap > dias_del_mes(mesp, aniop):
        return False
    else:
        return True


def leer_fecha():
    while True:
        dia_sal = int(input("Dia: "))
        mes_sal = int(input("Mes: "))
        anio_sal = int(input("Año: "))
        if not validar_fecha(dia_sal, mes_sal, anio_sal):
            print("Fecha no válida")
        else:
            break
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
