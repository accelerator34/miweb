import random
import time

def mostrarIntroduccion():
	print("Estás en una Tierra llena de dragones. Frente a tí")
	time.sleep(1)
	print("Hay dos cuevas. en una de ellas, el dragón es generoso y")
	time.sleep(1)
	print("amigable y compartirá su tesoro contigo. El otro dragón")
	time.sleep(1)
	print("codicioso y está hambriento, y te devorará inmediatamente")
	time.sleep(1)

def explorarCuevas(cuevaElegida):
	print("Te aproximas a la cueva...")
	time.sleep(2)
	print("Es oscura y espeluznante...")
	time.sleep(2)
	print("¡Un gran dragon aparece súbitamente frente a ti! Abre sus fauces y...")
	time.sleep(2)

mostrarIntroduccion()
cuevaElegida = str(input("¿A cual cueva quieres entrar? (1 o 2): "))

if cuevaElegida == "1":
	explorarCuevas(cuevaElegida)
	print("¡Te regala su tesoro!")
elif cuevaElegida == "2":
	explorarCuevas(cuevaElegida)
	print("¡Te engulle de un bocado!")
else:
	print("has introducido un valor inexistente")

jugarDeNuevo = input("¿Quieres jugar de nuevo? ")

while jugarDeNuevo == "si" or jugarDeNuevo == "s":
	mostrarIntroduccion()
	cuevaElegida = str(input("¿A cual cueva quieres entrar? (1 o 2): "))

	if cuevaElegida == "1":
		explorarCuevas(cuevaElegida)
		print("¡Te regala su tesoro!")
	elif cuevaElegida == "2":
		explorarCuevas(cuevaElegida)
		print("¡Te engulle de un bocado!")
	else:
		print("has introducido un valor inexistente")

	jugarDeNuevo = input("¿Quieres jugar de nuevo? ")

print("Juego Terminado.")

