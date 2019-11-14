# Ejercicio 16
# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los
# dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
# alcanzará el vehículo más rápido al otro.
print("****************************")
print("* SECCION 3 - EJERCICIO 16 *")
print("****************************")

velocidad1 = float(input("Indique la velocidad del coche 1 (km/h)    : "))
velocidad2 = float(input("Indique la velocidad del coche 2 (km/h)    : "))
distancia = float(input("Indique la distancia entre ambos coches (km): "))

tiempo = distancia / (velocidad1 - velocidad2)
tiempo = tiempo * 60

print("El coche que va detras alcanzara al otro en ", tiempo, " minutos")
