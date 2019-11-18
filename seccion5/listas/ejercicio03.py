# Ejercicio 3
#
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas = []

for i in range(1, 6):
    while True:
        nota = int(input("Introduzca la nota {0} del alumno: ".format(i)))
        if nota < 0 or nota > 10:
            print("ERROR: La nota introducida solo puede estar entre 0 y 10")
        else:
            notas.append(nota)
            break

print("Notas: ", end="")
for i in notas:
    print(i, " ", end="")
print()
print("Nota media: ", sum(notas)/len(notas))
print("Nota mas alta: ", max(notas))
print("Nota mas baja: ", min(notas))
