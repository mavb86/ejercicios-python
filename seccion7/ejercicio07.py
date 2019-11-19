# Ejercicio 7
#
# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero
# si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha
# intentado hacer login y si no se ha podido hacer login incremente este valor.
#
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login,
# solamente tenemos tres oportunidades para intentarlo.


def login(usuario, password, intentos):
    intentos += 1
    if usuario == "usuario1" and password == "asdasd":
        return True, intentos
    else:
        return False, intentos


intentos = 0
while True:
    usuario = input("Introduzca el nombre de usuario: ")
    password = input("Introduzca la contraseña: ")
    entrar, intentos = login(usuario, password, intentos)
    if entrar or intentos == 3:
        break
    if not entrar:
        print("ERROR: No se ha podido loguear correctamente, le quedan {0} intentos".format(3 - intentos))
if entrar:
    print("Has accedido al sistema")
else:
    print("No has conseguido entrar en el sistema en el número de intentos permitidos")
