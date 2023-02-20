# Imports go at the top
from microbit import *

i = 0
lista_numeros = [1, 2, 3, 4, 5]
total = 0

for i in lista_numeros:
    total = total + i

display.scroll(total)