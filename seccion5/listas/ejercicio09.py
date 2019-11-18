# Ejercicio 9
#
# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#
#     La temperatura media de cada día
#
#     Los días con menos temperatura
#
#     Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
#     si no existe ningún día se muestra un mensaje de información.

temperaturas = []

# Rellenamos las temperaturas maximas y mínimas de los 5 días
for i in range(1, 6):
    temperatura = []
    temperatura.append(int(input("Día {0}. Temperatura máxima: ".format(i))))
    temperatura.append(int(input("Día {0}. Temperatura mínima: ".format(i))))
    temperaturas.append(temperatura)

# Mostrar temperatura media
print()
print("Temperaturas medias")
print("-------------------")

i = 1
for temperatura in temperaturas:
    print("Día {0}. Temperatura media: {1}: ".format(i, sum(temperatura) / len(temperatura)))
    i += 1

# Calcular temperatura mínima más pequeña
# Supongo que es la primera
temp_min = temperaturas[0][1]
for temperatura in temperaturas:
    if temperatura[1] < temp_min:
        temp_min = temperatura[1]

# Mostrar los días con menos temperatura
print()
print("Días con menos temperatura")
print("--------------------------")
i = 1
for temperatura in temperaturas:
    if temperatura[1] == temp_min:
        print("Día {0}".format(i))
    i += 1

# Días con temperatura máxima
existe_temperatura = False
print()
print("Días con temperatura máxima")
print("---------------------------")
temp_max = int(input("Introduce una temperatura: "))
i = 1
for temperatura in temperaturas:
    if temperatura[0] == temp_max:
        print("Día {0}".format(i))
        existe_temperatura = True
    i += 1
if not existe_temperatura:
    print("No hay ningún día con dicha temperatura.")
