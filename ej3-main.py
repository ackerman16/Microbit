# Imports go at the top
from microbit import *
import music

while True:
    if button_a.is_pressed():
        music.play(music.NYAN)
        display.show(Image.HEART)
        sleep(500)
    elif button_b.is_pressed():
        music.play(music.DADADADUM)
        display.show(Image.GHOST)
        sleep(500)
        