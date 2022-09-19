import random
import time

def mostrarIntroduccion():
	print("Estás en una Tierra llena de dragones. Frente a tí")
	print("Hay dos cuevas. en una de ellas, el dragón es generoso y")
	print("amigable y compartirá su tesoro contigo. El otro dragón")
	print("codicioso y está hambriento, y te devorará inmediatamente")

def elegirCuevas():
	cueva = str(input("¿A qué cueva quieres entrar? (1 o 2)"))

def explorarCuevas(cuevaElegida):
	print("Te aproximas a la cueva...")
	time.sleep(2)
	print("Es oscura y espeluznante...")
	time.sleep(2)
	print("¡Un gran dragon aparece súbitamente frente a ti! Abre sus fauces y...")
	time.sleep(2)

#cuevaAmigable = random.randit(1, 2)

#if cuevaElegida == str(cuevaAmigable):
	#print("¡Te regala su tesoro!")
#else:
	#print("¡Te engulle de un bocado!")

#jugarDeNuevo = "si"
#while jugarDeNuevo == "si" or jugarDeNuevo =="s":

	#mostrarIntroduccion()

	#numeroDeCueva = elegirCuevas()

	#explorarCuevas(numeroDeCueva)

	#jugarDeNuevo = input("¿Quieres jugar denuevo? (si o no)")