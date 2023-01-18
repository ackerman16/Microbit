from microbit import *

n = 1
uno = Image("09090:99999:99999:09990:00900")
dos = Image("99999:99999:09990:00900:09090")
tres = Image("99999:09990:00900:09090:99999")
cuatro = Image("09990:00900:09090:99999:9999")
cinco = Image("00900:09090:99999:99999:09990")

while True:
    display.show(uno)
    sleep(200)
    display.show(dos)
    sleep(200)
    display.show(tres)
    sleep(200)
    display.show(cuatro)
    sleep(200)
    display.show(cinco)
    sleep(200)
    
   