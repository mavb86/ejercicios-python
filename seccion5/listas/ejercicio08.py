# Ejercicio 8
#
# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y
# la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*)
# Al finalizar se mostrará los siguientes datos:
#
#     Todos lo alumnos mayores de edad.
#
#     Los alumnos mayores (los que tienen más edad)

nombres = []
edades = []

while True:
    nombre = input("Introduzca el nombre del alumno (introduzca * para salir: ")
    if nombre == "*":
        break
    else:
        nombres.append(nombre)
        edad = int(input("Introduza la edad del alumno {0}: ".format(nombre)))
        edades.append(edad)

edad_maxima = max(edades)

print("Alumnos mayores de edad")
print("-----------------------")
for nombre, edad in zip(nombres,edades):
    if edad >= 18:
        print(nombre)

print("Alumnos mayores")
print("---------------")
for nombre, edad in zip(nombres, edades):
    if edad == edad_maxima:
        print(nombre)
