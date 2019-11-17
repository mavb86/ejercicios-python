# Ejercicio 16
#
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además,
# calcule cuánto pagó la empresa por los N empleados.


trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?:"))
sueldo_por_hora = float(input("Introduzca el sueldo por hora:"))

horas_acum = 0

for trabajador in range(1, trabajadores + 1):
    horas_x_semana = int(input("¿Cuántas horas ha trabajado el trabajador %d durante la semana ?:" % trabajador))
    horas_acum += horas_x_semana
    print("El trabajador %d tiene de sueldo %f" % (trabajador, horas_x_semana * sueldo_por_hora))
print("El pago a los %d trabajadores es: %f" % (trabajadores, horas_acum * sueldo_por_hora))

