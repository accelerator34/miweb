"""indice = int(input("ingrese un indice: "))

try:
    mi_lista = [1,2,3,4]
    print(mi_lista[indice])
except:
    print("Por favor ingrese un indice valido")
else:
    print("has ingresado los datos correctamentes")
finally:
    print("has finalizado el programa")"""

letras = "AKLSKKNDSA@asdasd"
for letra in letras:
    print("El valor de {} es {}".format(letra, ord(letra)))
    