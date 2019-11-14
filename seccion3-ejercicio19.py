# Ejercicio 19
# Escribir un algoritmo para calcular la nota final de un estudiante,
# considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0.
# Imprime el resultado obtenido por el estudiante.

print("****************************")
print("* SECCION 3 - EJERCICIO 19 *")
print("****************************")

resp_ok = int(input("¿Cuantas respuestas del alumno han sido correctas?"))
resp_nok = int(input("¿Cuantas respuestas del alumno han sido incorrectas?"))
resp_bla = int(input("¿Cuantas respuestas del alumno han sido en blanco?"))

print("La nota final del alumno es: ", (resp_ok * 5) + (resp_nok * -1))

