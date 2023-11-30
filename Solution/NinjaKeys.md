

``` py

import pyautogui
import time

time.sleep(5)
print("Pousse sur R pour recommencer")
pyautogui.keyDown('r')
pyautogui.keyUp('r')

time.sleep(0.1)
print("Sword")
pyautogui.keyDown('x')
pyautogui.keyUp('x')
time.sleep(0.1)
print("kunai")
pyautogui.keyDown('z')
pyautogui.keyUp('z')


time.sleep(0.1)
print("Aller à gauche")
pyautogui.keyDown('left')
pyautogui.keyUp('left')

time.sleep(0.1)
print("Sauter")
pyautogui.keyDown('up')
pyautogui.keyUp('up')

time.sleep(0.1)
print("Aller à droite")
pyautogui.keyDown('right')
pyautogui.keyUp('right')



print("Doubel saut")
pyautogui.keyDown('up')
pyautogui.keyUp('up')
time.sleep(0.1)
pyautogui.keyDown('up')
pyautogui.keyUp('up')
```
