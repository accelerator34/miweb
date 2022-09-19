saludar = input("Quieres saludar? ")

if saludar == "Yes":
    print("Saluda")
else:
    print("se va")


boleana = input("Quieres saludar denuevo?")

while boleana == "yes":
    if saludar == "Yes":
        print("Saluda")

    boleana = input("Quieres saludar denuevo?")
    if boleana != "Yes":
        break

print("Sigues tu camino")
