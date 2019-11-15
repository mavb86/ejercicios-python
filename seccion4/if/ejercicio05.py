# Ejercicio 5
#
# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd”
# se indica “Has entrado al sistema”, sino se da un error.

nombre = input("Introduzca su nombre de usuario: ")
password = input("Introduzca su contraseña: ")

if nombre == "pepe" and password == "asdasd":
    print("Has entrado en el sistema")
else:
    print("Los datos introducidos son incorrectos")
