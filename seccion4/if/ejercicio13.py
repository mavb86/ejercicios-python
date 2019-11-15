# Ejercicio 13
#
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Introduzca el dia: "))
mes = int(input("Introduzca el mes: "))
year = int(input("Introduzca el año: "))

dias_del_mes = 0

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_del_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_del_mes = 30
elif mes == 2:
    if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
        dias_del_mes = 29
    else:
        dias_del_mes = 28
else:
    print("Fecha incorrecta")

if dia < 0 or dia > dias_del_mes:
    print("Fecha incorrecta")
else:
    print("Fecha correcta")
