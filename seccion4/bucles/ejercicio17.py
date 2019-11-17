# Ejercicio 17
#
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Para esto, se registran los días que trabajó y las horas de cada día.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores
# y además calcule cuánto pagó la empresa por los N empleados.

trabajadores = int(input("Introduzca el número de trabajadores de la empresa: "))
sueldo_x_hora = float(input("Introduzca el sueldo por hora: "))

acum_horas_totales = 0

for trabajador in range(1, trabajadores + 1):
    acum_horas_empleado = 0
    dias = int(input("Introduzca los dias que ha trabajado el trabajador {0}: ".format(trabajador)))
    while dias < 1 or dias > 7:
        print("ERROR: Los valores posibles a introducir son de 1 a 7")
        dias = int(input("Introduzca los dias que ha trabajado el trabajador {0}: ".format(trabajador)))
    for dia in range(1, dias + 1):
        horas = int(input("Introduzca las horas trabajadas por el trabajador {0} el dia {1}: ".format(trabajador, dia)))
        while horas < 1 or horas > 8:
            print("ERROR: Los valores posibles a introducir son de 1 a 8")
            horas = int(input("Introduzca las horas trabajadas por el trabajador {0} el dia {1}: ".format(trabajador, dia)))
        acum_horas_totales += horas
        acum_horas_empleado += horas
    print("El sueldo semanal del empleado", trabajador, " es de ", sueldo_x_hora * acum_horas_empleado,
          " por los {0} días trabajados y las {1} horas trabajadas".format(dias, acum_horas_empleado))

print("Para ", trabajadores, "trabajadores la empresa debera abonar ", sueldo_x_hora * acum_horas_totales,
      "por las ", acum_horas_totales, " horas totales trabajadas")

