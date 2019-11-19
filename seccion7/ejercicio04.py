# Ejercicio 4
#
# Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y
# devuelve una cadena con un espacio adicional tras cada letra.
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.


def convertir_espaciado(texto):
    texto_espaciado = texto.replace("", " ")
    return texto_espaciado.strip()


cadena = input("Introduce una cadena por teclado:")
print("La cadena añadiendo espacios es: ", convertir_espaciado(cadena))
