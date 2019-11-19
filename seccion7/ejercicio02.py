# Ejercicio 2
#
# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.


def esmultiplo(num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


num1 = int(input("Escriba el número 1: "))
num2 = int(input("Escriba el número 2: "))

if esmultiplo(num1, num2):
    print("El numero {0} es múltiplo del número {1}".format(num1, num2))
else:
    print("El numero {0} no es múltiplo del número {1}".format(num1, num2))

