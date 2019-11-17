# Ejercicio 15
#
# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €,
# el tercero 40 € y así sucesivamente.
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de
# lo que pagó después de los 20 meses.

mensualidad = 5
acum_mensualidad = 0
for mes in range(1, 21):
    mensualidad = mensualidad * 2
    acum_mensualidad += mensualidad
    print("Mes ", mes, " - Coste: ", mensualidad)
print("En total ha pagado: ", acum_mensualidad)
