# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero
# obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes
# tomando en cuenta su sueldo base y comisiones.

print("***************************")
print("* SECCION 3 - EJERCICIO 8 *")
print("***************************")

salario_base = float(input("Indique el sueldo base del trabajador: "))

comisiones = salario_base * 30 / 100

print("El trabajador recibira en la nomina los siguientes conceptos:")
print("-Salario base  =", salario_base)
print("-Comisiones    =", comisiones)
print("-Salario total =", salario_base + comisiones)
