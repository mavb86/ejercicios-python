# Ejercicio 14
#
# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva,
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2.
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá
# un productor por la uva que entrega en un embarque, considerando lo siguiente:
# si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2.
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.
# Realice un algoritmo para determinar la ganancia obtenida.

precio_inicial = float(input("Indique el precio inicial por kilos de la uva (centimos): "))
kilos = float(input("Indique los kilos de uva: "))
tipo = input("Indique el tipo de uva (A/B)").upper()

if tipo != "A" and tipo != "B":
    print("El tipo de uva introducido es incorrecto")
else:
    tamano = int(input("Indique el tamaño de la uva (1/2): "))
    if tamano != 1 and tamano != 2:
        print("El tamaño introducido de la uva es incorrecto")
    else:
        if tipo == "A":
            if tamano == 1:
                precio_inicial = precio_inicial + 20
            else:
                precio_inicial = precio_inicial + 30
        else:
            if tamano == 1:
                precio_inicial = precio_inicial - 30
            else:
                precio_inicial = precio_inicial - 50
        precio_final = precio_inicial * kilos
        print("La ganancia es %.2f euros." % (precio_final / 100))
