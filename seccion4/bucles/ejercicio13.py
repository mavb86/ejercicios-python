# Ejercicio 13
#
# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y
# requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

sueldo_hora = float(input("Introduce el sueldo por hora: "))
horas_acum = 0

for dia in range(1,7):
    horas = int(input("¿Cuantas horas ha trabajado el día %d ?:" % dia))
    horas_acum += horas

print("El trabajador ha trabajado ", horas_acum, " horas.")
print("El sueldo a percibir por esas horas es de: ", sueldo_hora * horas_acum)


