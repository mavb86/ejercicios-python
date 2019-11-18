# Ejercicio 13
#
# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene,
# y los kilómetros que conducen cada día de la semana.
#
# Para guardar esta información se van a utilizar dos arreglos:
#
#     Nombre: Lista para guardar los nombres de los conductores.
#
#     kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
#
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
#
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

nombres = []
kms = []
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

while True:
    conductores = int(input("¿Cuantos conductores tiene la empresa?: "))
    if conductores > 0:
        break
    else:
        print("ERROR: La empresa debe de tener algún conductor")

for conductor in range(0, conductores):
    nombre = input("Introduzca el nombre del conductor {0}: ".format((conductor + 1)))
    nombres.append(nombre)
    kms_dias = []
    for dia in range(0, 7):
        kms_dias.append(int(input("Introduzca los kms recorridos el {0} por el conductor {1}: ".format(dias[dia], nombre))))
    kms.append(kms_dias)

total_kms = []
for km in kms:
    total_kms.append(sum(km))

for nombre, km in zip(nombres, total_kms):
    print("{0}  ha realizado {1} kms.".format(nombre, km))
