#Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final.

import  random
numero_secreto = random.randint(1,10)
adivinanza = 0
while adivinanza!= numero_secreto:
    adivinanza= int(input('Ingrese un número del 1 al 10 para adivinar el número secreto: '))
    if  adivinanza!= numero_secreto:
        print('Intenta nuevamente')
    else: 
        print('Felicidades adivinaste')
