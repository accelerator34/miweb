oracion = input("Introduce una oracion minimo 3 palabras: ")
espacioss = 0

for espacios in oracion:
    if espacios == " ":
        espacioss += 1

espacioss = espacioss + 1
print(f"hay {espacioss} palabras en total")