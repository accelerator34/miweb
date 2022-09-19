palabra = input("ingresa una palabra para codificarla: ")

def codificar(palabra):
    for letras in palabra:
        letras = ord(letras)
        letras = letras + 1
        Letras = chr(letras)
        Palabras = Letras
        print(Palabras, end="")

def decodificar(palabra):
    for letras in palabra:
        letras = ord(letras)
        letras = letras - 1
        Letras = chr(letras)
        Palabras = Letras
        print(Palabras, end="")
decodificar(palabra)
"""
codificar(palabra)
palabra = input("introduce la palabra: ")
for letra in palabra:
    print("El valor de", letra, " es " + str(ord(letra)))"""