# Calcular la media de tres números pedidos por teclado
import stats as stats

print("***************************")
print("* SECCION 3 - EJERCICIO 6 *")
print("***************************")

print("Se le van a solicitar 3 números y calcularemos la media por used")

numero1 = float(input("Numero 1:"))
numero2 = float(input("Numero 2:"))
numero3 = float(input("Numero 3:"))

numeros_recibidos = [numero1, numero2, numero3]

media = stats.mean(numeros_recibidos)

print("La media de los números que ha introducido es:", media)
