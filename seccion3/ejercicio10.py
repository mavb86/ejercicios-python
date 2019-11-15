# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone
# de los siguientes porcentajes:
#
#     55% del promedio de sus tres calificaciones parciales.
#
#     30% de la calificación del examen final.
#
#     15% de la calificación de un trabajo final.

import statistics as stats

print("****************************")
print("* SECCION 3 - EJERCICIO 10 *")
print("****************************")

parcial1 = float(input("Inserte el valor de la nota del primer parcial    : "))
parcial2 = float(input("Inserte el valor de la nota del segundo parcial   : "))
parcial3 = float(input("Inserte el valor de la nota del tercer parcial    : "))
examen_final = float(input("Inserte el valor de la nota del examen final  : "))
trabajo_final = float(input("Inserte el valor de la nota del trabajo final: "))

parciales = [parcial1, parcial2, parcial3]
media_parciales = stats.mean(parciales)

parciales55 = media_parciales * 55 / 100
examen_final33 = examen_final * 33 / 100
trabajo_final15 = trabajo_final * 15 / 100

print("La nota final del alumno es:", parciales55 + examen_final33 + trabajo_final15)
