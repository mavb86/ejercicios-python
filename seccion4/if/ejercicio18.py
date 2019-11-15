# Ejercicio 18
#
# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
# Si introducimos otro número nos da un error.

dia_n = int(input("Indique el dia de la semana: "))

if 0 < dia_n < 7:
    dia_l = ""
    if dia_n == 1:
        dia_l = "Lunes"
    elif dia_n == 2:
        dia_l = "Martes"
    elif dia_n == 3:
        dia_l = "Miercoles"
    elif dia_n == 4:
        dia_l = "Jueves"
    elif dia_n == 5:
        dia_l = "Viernes"
    elif dia_n == 6:
        dia_l = "Sabado"
    elif dia_n == 7:
        dia_l = "Domingo"
    print("El dia de la semana que has elegido es: ", dia_l)
else:
    print("El dia que has introducido es erroneo")

