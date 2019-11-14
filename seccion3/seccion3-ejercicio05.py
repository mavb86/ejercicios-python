#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius

gradosF = float(input("Escriba el valor de los grados Fahrenheit que quiere convertir a Celsius:"))
gradosC = (gradosF-32)*5/9

print("El resultado en grados Celsius es: ", gradosC)