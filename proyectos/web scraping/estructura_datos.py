#una lista es un conjunto ordenado de datos
#2 maneras de eliminar datos en una lista
lista = ["losjuegos del hambre", "relleno", 34]
lista.remove(34)#esta para cuando sabemos que objeto queremos eliminar

#manera 2
lista2 = ["los juegos del calamar", "norelleno", 43]
del lista2[2]#esta para cuando no sepamos el valor pero si la posicion del elemento
#añadir valor
lista.append(["holoa", "hello"])#este aumenta la longitud de un elemento
print(lista)
lista2.extend(["hello", "hola"])#y este los divide en diferentes elementos
print(lista2)
#insertar
lista.insert(1, "fernan")#posicion y luego dato
print(lista)
#saber la posicion
print(lista.index("fernan"))
#saber si esta en una lista
print("fernan" in lista)
#esto es para obtener y borrar un valor
lista.pop(1)
print(lista)
#saber cuantas veces se repite un valor
print(lista.count("fernan"))
#saber cuantos elementos contiene
print(len(lista))
#para revertir el orden de la lista
print(lista.reverse())