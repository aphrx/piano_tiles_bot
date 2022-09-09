import time
import pyautogui
import numpy as np
from pynput.mouse import Listener, Button, Controller
from PIL import ImageGrab

mouse = Controller()
mousePositions = []
keys = ['d', 'f', 'j', 'k']
BLACK = [5, 5, 5]
BLUE_UPPER = [60, 165, 205]
BLUE_LOWER = [50, 150, 190]

def on_click(x, y, button, isPressed):
    if isPressed and button == Button.left:
        mousePositions.append((x, y))
    if len(mousePositions) == 4:
        listener.stop()

print("Click the scan locations from left to right")

with Listener(on_click=on_click) as listener:
    listener.join()

print("Bot will start in 5 seconds")
time.sleep(5)

print("Starting")
while True:
    img = ImageGrab.grab()
    for index, pos in enumerate(mousePositions):
        colour = np.array(img.getpixel(pos))
        if (colour <= BLACK).all() or ((colour <= BLUE_UPPER).all() and (colour >= BLUE_LOWER).all()):
            pyautogui.press(keys[index])