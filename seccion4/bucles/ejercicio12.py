# Ejercicio 12
#
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes
# deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

ahorro_acum = 0
for mes in range(1,13):
    ahorro_mes = float(input("¿Cuánto has ahorrado en el mes %d ?:" % mes))
    ahorro_acum += ahorro_mes
    print("Actualmente, llevas ahorrado: ", ahorro_acum)
