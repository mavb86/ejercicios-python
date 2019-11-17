# Ejercicio 8
#
# Escribe un programa que pida el limite inferior y superior de un intervalo.
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0.

# Cuando termine el programa dará las siguientes informaciones:
#
#     La suma de los números que están dentro del intervalo (intervalo abierto).
#
#     Cuantos números están fuera del intervalo.
#
#     He informa si hemos introducido algún número igual a los límites del intervalo.

repetir = True
while repetir:
    lim_inf = int(input("Introduzca el límite inferior: "))
    lim_sup = int(input("Introduzca el límite superior: "))
    if lim_inf < lim_sup:
        repetir = False
    else:
        print("ERROR: No puede introducir un numero en el límite inferior superior al límite superior")

suma = 0
igual = 0
dentro = 0
fuera = 0

repetir = True
while repetir:
    num = int(input("Introduzca un número (0 para salir)"))
    if num != 0:
        if num >= lim_inf and num <= lim_sup:
            if num == lim_inf or num == lim_sup:
                igual += 1
                dentro += 1
            else:
                suma += num
                dentro += 1
        else:
            fuera += 1
    else:
        repetir = False

print("Sume de los números dentro del intervalo: ", suma)
print("Números dentro del intervalo: ", dentro)
print("Números fuera del intervalo: ", fuera)
if igual > 0:
    print("Se han introducido números iguales a los límites del intervalo")
else:
    print("No se han introducido números iguales a los límites del intervalo")
