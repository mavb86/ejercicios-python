# Ejercicio 20
#
# Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central,
# América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y
# la zona a la que va dirigido. Lo anterior se muestra en la tabla:
#
# ZonaUbicaciónCosto/gramo
# 1América del Norte24.00 euros
# 2América Central20.00 euros
# 3América del Sur21.00 euros
# 4Europa10.00 euros
# 5Asia18.00 euros
#
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados,
# esto por cuestiones de logística y de seguridad.
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

zona = int(input('''Indique la zona a donde enviara el paquete:
                  "1" - America del Norte
                  "2" - America Central
                  "3" - America del Sur
                  "4" - Europa
                  "5" - Asia
             '''))

if 0 < zona < 6:
    gramos = int(input("Indique el numero de gramos del paquete: "))
    if 0 < gramos < 5000:
        coste_gramo = 0
        if zona == 1:
            coste_gramo = 24
        elif zona == 2:
            coste_gramo = 20
        elif zona == 3:
            coste_gramo = 21
        elif zona == 4:
            coste_gramo = 10
        elif zona == 5:
            coste_gramo = 18
        print("El coste del envio es de ", gramos * coste_gramo, " euros")
    else:
        if gramos > 5000:
            print("El paquete sobreapasa los 5kg y no podra ser enviado")
        else:
            print("El dato introducido para el peso es incorrecto")
else:
    print("La zona de envio seleccionada es incorrecta")

