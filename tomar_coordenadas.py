import pyautogui as pa
import keyboard
import time
import os
print(pa.position())

fileName = r"coordenadas.txt"
f = open(fileName, "a")

numero = 0
while True:
    if keyboard.is_pressed('C'):
        print(str(numero) + "-" + str(pa.position().x) + "," + str(pa.position().y))
        #f.write(str(numero) + "-" + str(pa.position().x) + "," + str(pa.position().y))
        numero += 1
        time.sleep(0.2)
    if keyboard.is_pressed('Q'):
        break

f.close()
