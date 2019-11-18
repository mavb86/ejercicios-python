# Ejercicio 4
#
# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase
# y las notas que han obtenido.
# Cada alumno puede tener distinta cantidad de notas.
# Guarda la información en un diccionario cuya claves serán los nombres de los alumnos
# y los valores serán listas con las notas de cada alumno.
#
# El programa pedirá el número de alumnos que vamos a introducir,
# pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.
# Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

alumnos = {}
num_alumnos = int(input("Indique la cantidad de alumnos que quiere guardar: "))
for num in range(num_alumnos):
    alumno = input("Indique el nombre del alumno: ")
    while alumno in alumnos:
        print("El alumno ya existe")
        alumno = input("Indique el nombre del alumno: ")
    notas = []
    while True:
        nota = int(input("Teclee la nota del alumno (negativa para terminar): "))
        if nota < 0:
            break
        else:
            notas.append(nota)
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("{0} ha sacado de nota media {1}".format(alumno, sum(notas) / len(notas)))
