# Imports go at the top
from microbit import *
import random

vocales = ['A', 'E', 'I', 'O', 'U']
consonantes = ['B', 'C', 'D', 'F', 'G']
total_letras = 9

while total_letras>0:
    if button_a.was_pressed():
        vocal_aleatoria = vocales[random.randint(0,len(vocales)-1)]
        display.show(vocal_aleatoria)
        total_letras = total_letras -1
        sleep(1000)
    elif button_b.was_pressed():
        consonante_aleatoria = consonantes[random.randint(0,len(consonantes)-1)]
        display.show(consonante_aleatoria)
        total_letras = total_letras -1
        sleep(1000)
    else:
        display.show("?")

display.scroll('Fin')

temporizador = 20
while temporizador>0:
    temporizador = temporizador - 1
    display.scroll(temporizador, delay=30)
    sleep(1000)