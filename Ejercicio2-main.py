# Imports go at the top
from microbit import *

i = 0
lista_animales = ['Perro', 'Gato', 'Caballo', 'Oveja']

for i in lista_animales:
    display.scroll(i)
    sleep(500)
