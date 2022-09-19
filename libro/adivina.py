#Este es mi primer juego, a ver que tal sale
import random

intentosRealizados = 0

miNombre = input('¿Cómo te llamas? ')

numero = random.randint(1, 20)
print('Bueno,' + miNombre + ', estoy pensando en un numero entre el 1 y el 20')

while intentosRealizados < 6:
    print('intenta adivinar.')
    estimacion = int(input('¿Cual es tu estimacion? '))

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Tu estimacion es muy baja.')

    if estimacion > numero:
        print('Tu estimacion es muy alta')
    
    if estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('Buen trabajo,', miNombre, '¡Has adivinado mi numero en!', intentosRealizados)

if estimacion != numero:
    numero = str(numero)
    print('Pues no. El numero que estaba pensando era', numero)
