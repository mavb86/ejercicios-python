# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

print("***************************")
print("* SECCION 3 - EJERCICIO 7 *")
print("***************************")

minutos = int(input("Introduzca el numero de minutos para transformar en horas y minutos:"))

res_horas = minutos // 60
res_min = minutos % 60

print(res_horas, " horas y ", res_min, " minutos")
