from microbit import *

#Contar las veces que se pulsa el botón a en 13 segundos
sleep(13000)
display.scroll(str(button_a.get_presses()))
