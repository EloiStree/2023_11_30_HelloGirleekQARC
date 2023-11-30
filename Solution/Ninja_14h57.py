import pyautogui
import time
import keyboard


etat_precedent=False
etat_actuel=False

def double_saut():
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')
    time.sleep(0.1)
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')

    #1
def bouger_a_droite(temp_second):
    pyautogui.keyDown('right')
    time.sleep(temp_second)
    pyautogui.keyUp('right')

def bouger_a_left(temp_second):
    pyautogui.keyDown('left')
    time.sleep(temp_second)
    pyautogui.keyUp('left')
    
def bouger_direction(direction, temp_second):
    pyautogui.keyDown(direction)
    time.sleep(temp_second)
    pyautogui.keyUp(direction)

def bouger_a_left(temp_second):
    pyautogui.keyDown('left')
    time.sleep(temp_second)
    pyautogui.keyUp('left')

    
#3
def sacade(temp_de_sacade): 
    bouger_a_droite(1)
    time.sleep(temp_de_sacade)
    bouger_a_droite(0.2)
    time.sleep(temp_de_sacade)
    bouger_a_droite(1)
    time.sleep(temp_de_sacade)
    bouger_a_droite(0.2)
    


while True:
    etat_precedent= etat_actuel
    etat_actuel= keyboard.is_pressed('space')
    
    print(".")
    time.sleep(0.1)
    # True  False   not True False
    if etat_precedent != etat_actuel:
        if etat_actuel==True:
            print(f"Enfoncé !!")
            double_saut()
            # sacade(3)
            bouger_direction('left',0.2)
            bouger_direction('right',0.4)
            bouger_direction('up',0.1)
            time.sleep(0.1)
            bouger_direction('up',0.1)
            
        if etat_actuel==False:
            print(f"J'ai relaché !!")



time.sleep(5)
pyautogui.keyDown('r')
pyautogui.keyUp('r')

time.sleep(0.1)
pyautogui.keyDown('x')
pyautogui.keyUp('x')
time.sleep(0.1)
pyautogui.keyDown('z')
pyautogui.keyUp('z')


time.sleep(0.1)
pyautogui.keyDown('left')
pyautogui.keyUp('left')

time.sleep(0.1)
pyautogui.keyDown('up')
pyautogui.keyUp('up')

time.sleep(0.1)
pyautogui.keyDown('right')
pyautogui.keyUp('right')


