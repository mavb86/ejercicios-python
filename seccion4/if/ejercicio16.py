# Ejercicio 16
# La política de cobro de una compañía telefónica es: cuando se realiza una llamada,
# el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
# los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %,
# y en turno de tarde, 10 %.
# Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

minutos = int(input("Indique los minutos de la llamada: "))
es_domingo = input("¿Es domingo? (S/N): ").upper()

if es_domingo == "N":
    turno = input("¿Qué turno: Mañana o Tarde? (M/T)?:")
if minutos < 5:
    coste = minutos * 100
else:
    if minutos < 8:
        coste = (minutos - 5) * 80 + 500
    else:
        if minutos < 10:
            coste = (minutos - 8) * 70 + 240 + 500
        else:
            coste = (minutos - 10) * 50 + 140 + 240 + 500
if es_domingo == "S":
    coste = coste + coste * 0.03
else:
    if turno == "M":
        coste = coste + coste * 0.15
    else:
        coste = coste + coste * 0.10

print("El coste de la llamada: %.2f euros." % (coste / 100))
