from XInput import *

import ctypes
import pyvjoy
import pyautogui
import time

# WARNING
# - YOU MUST HAVE INSTALL VJOY ON YOUR COMPUTER
# - WORK WITH XINPUT CONTROLLER
# - YOU MUST HZVE INSTALL PYTHON ON YOUR COMPUTER
# - YOU MUST HAVE INSTALL PYTHON PACKAGE:
# - pip install XInput-Python
# - pip install pyvjoy
# - pip install pyautogui


try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk



# What force does trigger of the Xbox need to be used to go forward
trigger_sensibility=0.05



root = tk.Tk()
root.title("XInput")
canvas = tk.Canvas(root, width= 600, height = 400, bg="white")
canvas.pack()

set_deadzone(DEADZONE_TRIGGER,10)

hide_cursor=False


def switch_mouse_hide():
    global hide_cursor
    hide_cursor = not hide_cursor
    ctypes.windll.user32.ShowCursor(not hide_cursor)


class Controller:
    def __init__(self, center):
        self.center = center

        self.on_indicator_pos = (self.center[0], self.center[1] - 50)

        self.on_indicator = canvas.create_oval(((self.on_indicator_pos[0] - 10, self.on_indicator_pos[1] - 10), (self.on_indicator_pos[0] + 10, self.on_indicator_pos[1] + 10)))
        
        self.r_thumb_pos = (self.center[0] + 50, self.center[1] + 20)

        r_thumb_outline = canvas.create_oval(((self.r_thumb_pos[0] - 25, self.r_thumb_pos[1] - 25), (self.r_thumb_pos[0] + 25, self.r_thumb_pos[1] + 25)))

        r_thumb_stick_pos = self.r_thumb_pos

        self.r_thumb_stick = canvas.create_oval(((r_thumb_stick_pos[0] - 10, r_thumb_stick_pos[1] - 10), (r_thumb_stick_pos[0] + 10, r_thumb_stick_pos[1] + 10)))

        self.l_thumb_pos = (self.center[0] - 100, self.center[1] - 20)

        l_thumb_outline = canvas.create_oval(((self.l_thumb_pos[0] - 25, self.l_thumb_pos[1] - 25), (self.l_thumb_pos[0] + 25, self.l_thumb_pos[1] + 25)))

        l_thumb_stick_pos = self.l_thumb_pos

        self.l_thumb_stick = canvas.create_oval(((l_thumb_stick_pos[0] - 10, l_thumb_stick_pos[1] - 10), (l_thumb_stick_pos[0] + 10, l_thumb_stick_pos[1] + 10)))

        self.l_trigger_pos = (self.center[0] - 120, self.center[1] - 70)

        l_trigger_outline = canvas.create_rectangle(((self.l_trigger_pos[0] - 5, self.l_trigger_pos[1] - 20), (self.l_trigger_pos[0] + 5, self.l_trigger_pos[1] + 20)))

        l_trigger_index_pos = (self.l_trigger_pos[0], self.l_trigger_pos[1] - 20)

        self.l_trigger_index = canvas.create_rectangle(((l_trigger_index_pos[0] - 10, l_trigger_index_pos[1] - 5), (l_trigger_index_pos[0] + 10, l_trigger_index_pos[1] + 5)))

        self.r_trigger_pos = (self.center[0] + 120, self.center[1] - 70)

        r_trigger_outline = canvas.create_rectangle(((self.r_trigger_pos[0] - 5, self.r_trigger_pos[1] - 20), (self.r_trigger_pos[0] + 5, self.r_trigger_pos[1] + 20)))

        r_trigger_index_pos = (self.r_trigger_pos[0], self.r_trigger_pos[1] - 20)

        self.r_trigger_index = canvas.create_rectangle(((r_trigger_index_pos[0] - 10, r_trigger_index_pos[1] - 5), (r_trigger_index_pos[0] + 10, r_trigger_index_pos[1] + 5)))

        buttons_pos = (self.center[0] + 100, self.center[1] - 20)

        A_button_pos = (buttons_pos[0], buttons_pos[1] + 20)

        B_button_pos = (buttons_pos[0] + 20, buttons_pos[1])

        Y_button_pos = (buttons_pos[0], buttons_pos[1] - 20)

        X_button_pos = (buttons_pos[0] - 20, buttons_pos[1])

        self.A_button = canvas.create_oval(((A_button_pos[0] - 10, A_button_pos[1] - 10), (A_button_pos[0] + 10, A_button_pos[1] + 10)))

        self.B_button = canvas.create_oval(((B_button_pos[0] - 10, B_button_pos[1] - 10), (B_button_pos[0] + 10, B_button_pos[1] + 10)))

        self.Y_button = canvas.create_oval(((Y_button_pos[0] - 10, Y_button_pos[1] - 10), (Y_button_pos[0] + 10, Y_button_pos[1] + 10)))

        self.X_button = canvas.create_oval(((X_button_pos[0] - 10, X_button_pos[1] - 10), (X_button_pos[0] + 10, X_button_pos[1] + 10)))

        dpad_pos = (self.center[0] - 50, self.center[1] + 20)

        self.dpad_left = canvas.create_rectangle(((dpad_pos[0] - 30, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] + 10)), outline = "")

        self.dpad_up = canvas.create_rectangle(((dpad_pos[0] - 10, dpad_pos[1] - 30), (dpad_pos[0] + 10, dpad_pos[1] - 10)), outline = "")

        self.dpad_right = canvas.create_rectangle(((dpad_pos[0] + 10, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] + 10)), outline = "")

        self.dpad_down = canvas.create_rectangle(((dpad_pos[0] - 10, dpad_pos[1] + 10), (dpad_pos[0] + 10, dpad_pos[1] + 30)), outline = "")

        dpad_outline = canvas.create_polygon(((dpad_pos[0] - 30, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] - 30), (dpad_pos[0] + 10, dpad_pos[1] - 30),
                                              (dpad_pos[0] + 10, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] + 10), (dpad_pos[0] + 10, dpad_pos[1] + 10),
                                              (dpad_pos[0] + 10, dpad_pos[1] + 30), (dpad_pos[0] - 10, dpad_pos[1] + 30), (dpad_pos[0] - 10, dpad_pos[1] + 10), (dpad_pos[0] - 30, dpad_pos[1] + 10)),
                                             fill = "", outline = "black")

        back_button_pos = (self.center[0] - 20, self.center[1] - 20)

        self.back_button = canvas.create_oval(((back_button_pos[0] - 5, back_button_pos[1] - 5), (back_button_pos[0] + 5, back_button_pos[1] + 5)))

        start_button_pos = (self.center[0] + 20, self.center[1] - 20)

        self.start_button = canvas.create_oval(((start_button_pos[0] - 5, start_button_pos[1] - 5), (start_button_pos[0] + 5, start_button_pos[1] + 5)))

        l_shoulder_pos = (self.center[0] - 90, self.center[1] - 70)

        self.l_shoulder = canvas.create_rectangle(((l_shoulder_pos[0] - 20, l_shoulder_pos[1] - 5), (l_shoulder_pos[0] + 20, l_shoulder_pos[1] + 10)))

        r_shoulder_pos = (self.center[0] + 90, self.center[1] - 70)

        self.r_shoulder = canvas.create_rectangle(((r_shoulder_pos[0] - 20, r_shoulder_pos[1] - 10), (r_shoulder_pos[0] + 20, r_shoulder_pos[1] + 5)))

controllers = (Controller((150., 100.)),
               Controller((450., 100.)),
               Controller((150., 300.)),
               Controller((450., 300.)))

vjoy_device_id = 2  
joystick = pyvjoy.VJoyDevice(vjoy_device_id)



# ACTION TO DO IN GAME START ############


isPlayerLeft =True;

def set_as_left_handed():
    global isPlayerLeft
    if not isPlayerLeft:
        print(f"Left Handed") 
    isPlayerLeft=True

def set_as_right_handed():
    global isPlayerLeft
    if isPlayerLeft:
        print(f"Right Handed") 
    isPlayerLeft=False



def set_joystick(horizontal, vertical):
    print(f"X{event.x} Y{event.y}") 
    joystick.set_axis(pyvjoy.HID_USAGE_X, int(((horizontal+1)*0.5)*32767.0))    
    joystick.set_axis(pyvjoy.HID_USAGE_Y, int(((-vertical+1)*0.5)*32767.0))

def crouch():
    pyautogui.keyDown(char_key_move)
    pyautogui.keyUp(char_key_move)
    pyautogui.keyDown(char_key_move)
    pyautogui.keyUp(char_key_move)
    

def action_interact_start():
    pyautogui.keyDown('ctrlleft')
    print(" action_interact_start")
    
def action_interact_stop():
    pyautogui.keyUp('ctrlleft')
    print(" action_interact_stop")

def action_interact():
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyUp('ctrlleft')
    print(" action_interact")
    
def action_interact_stop():
    pyautogui.keyUp('ctrlleft')
    print(" action_interact_stop")
    
def action_move_start():
    joystick.set_button(1, 1)
    print(" action_move_start")

def action_move_stop():
    joystick.set_button(1, 0)
    print(" action_move_stop")
    
def switch_input_mode():
    pyautogui.keyDown('F3')
    pyautogui.keyUp('F3')
    print("switch_input_mode")

    
def ugly_crounch_input_mode():
    pyautogui.keyDown('F3')
    pyautogui.keyUp('F3')

    pyautogui.keyDown('shift')
    pyautogui.keyUp('shift')

    pyautogui.keyDown('F3')
    pyautogui.keyUp('F3')

    print("switch_input_mode")
def ugly_switch_input_mode():
    pyautogui.keyDown('F3')
    pyautogui.keyUp('F3')

    pyautogui.keyDown('ctrlright')
    pyautogui.keyUp('ctrlright')

    pyautogui.keyDown('F3')
    pyautogui.keyUp('F3')

    print("switch_input_mode")

    
def action_special_test_start():
    #Zone to try random experiment on press
    print(" action_sepcial_test_start")
    
def action_special_test_end():
    #Zone to try random experiment on release
    print(" action_sepcial_test_end")
    
# ACTION TO DO IN GAME END ###########


    
def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)



while 1:
    events = get_events()
    for event in events:
        controller = controllers[event.user_index]
        if event.type == EVENT_CONNECTED:
            canvas.itemconfig(controller.on_indicator, fill="light green")
            
        elif event.type == EVENT_DISCONNECTED:
            canvas.itemconfig(controller.on_indicator, fill="")
            
        elif event.type == EVENT_STICK_MOVED:
            if event.stick == LEFT:
                l_thumb_stick_pos = (int(round(controller.l_thumb_pos[0] + 25 * event.x,0)), int(round(controller.l_thumb_pos[1] - 25 * event.y,0)))
                canvas.coords(controller.l_thumb_stick, (l_thumb_stick_pos[0] - 10, l_thumb_stick_pos[1] - 10, l_thumb_stick_pos[0] + 10, l_thumb_stick_pos[1] + 10))
                set_joystick(event.x,event.y)

                
            elif event.stick == RIGHT:
                r_thumb_stick_pos = (int(round(controller.r_thumb_pos[0] + 25 * event.x,0)), int(round(controller.r_thumb_pos[1] - 25 * event.y,0)))
                canvas.coords(controller.r_thumb_stick, (r_thumb_stick_pos[0] - 10, r_thumb_stick_pos[1] - 10, r_thumb_stick_pos[0] + 10, r_thumb_stick_pos[1] + 10))
                
                set_joystick(event.x,event.y)

        elif event.type == EVENT_TRIGGER_MOVED:
            if event.trigger == LEFT:
                l_trigger_index_pos = (controller.l_trigger_pos[0], controller.l_trigger_pos[1] - 20 + int(round(40 * event.value, 0)))
                canvas.coords(controller.l_trigger_index, (l_trigger_index_pos[0] - 10, l_trigger_index_pos[1] - 5, l_trigger_index_pos[0] + 10, l_trigger_index_pos[1] + 5))
                print(f"JOYSTICK LEFT : {event.value}")
                if event.value>trigger_sensibility:
                    action_move_start()
                else:
                    action_move_stop()
                
            elif event.trigger == RIGHT:
                r_trigger_index_pos = (controller.r_trigger_pos[0], controller.r_trigger_pos[1] - 20 + int(round(40 * event.value, 0)))
                canvas.coords(controller.r_trigger_index, (r_trigger_index_pos[0] - 10, r_trigger_index_pos[1] - 5, r_trigger_index_pos[0] + 10, r_trigger_index_pos[1] + 5))
                print(f"JOYSTICK Right : {event.value}")
                if event.value>trigger_sensibility:
                    action_move_start()
                else:
                    action_move_stop()
               

        elif event.type == EVENT_BUTTON_PRESSED:
            if event.button == "LEFT_THUMB":
                canvas.itemconfig(controller.l_thumb_stick, fill="red")
            elif event.button == "RIGHT_THUMB":
                canvas.itemconfig(controller.r_thumb_stick, fill="red")

            elif event.button == "LEFT_SHOULDER":
                canvas.itemconfig(controller.l_shoulder, fill="red")
                set_as_left_handed()
                action_interact()
            elif event.button == "RIGHT_SHOULDER":
                canvas.itemconfig(controller.r_shoulder, fill="red")
                set_as_right_handed()
                action_interact()

            elif event.button == "BACK":
                canvas.itemconfig(controller.back_button, fill="red")
                switch_mouse_hide()
                switch_input_mode()
            elif event.button == "START":
                canvas.itemconfig(controller.start_button, fill="red")
                switch_input_mode()

            elif event.button == "DPAD_LEFT":
                canvas.itemconfig(controller.dpad_left, fill="red")
            elif event.button == "DPAD_RIGHT":
                canvas.itemconfig(controller.dpad_right, fill="red")
            elif event.button == "DPAD_UP":
                canvas.itemconfig(controller.dpad_up, fill="red")
            elif event.button == "DPAD_DOWN":
                canvas.itemconfig(controller.dpad_down, fill="red")

            elif event.button == "A":
                canvas.itemconfig(controller.A_button, fill="red")
                action_move_start()
                
            elif event.button == "B":
                canvas.itemconfig(controller.B_button, fill="red")
                ugly_crounch_input_mode() 

                
            elif event.button == "Y":
                canvas.itemconfig(controller.Y_button, fill="red")
                action_special_test_start()
                ugly_switch_input_mode()
                
            elif event.button == "X":
                canvas.itemconfig(controller.X_button, fill="red")
                action_interact()
                

        elif event.type == EVENT_BUTTON_RELEASED:
            if event.button == "LEFT_THUMB":
                canvas.itemconfig(controller.l_thumb_stick, fill="")
                
            elif event.button == "RIGHT_THUMB":
                canvas.itemconfig(controller.r_thumb_stick, fill="")

            elif event.button == "LEFT_SHOULDER":
                canvas.itemconfig(controller.l_shoulder, fill="")
            elif event.button == "RIGHT_SHOULDER":
                canvas.itemconfig(controller.r_shoulder, fill="")

            elif event.button == "BACK":
                canvas.itemconfig(controller.back_button, fill="")
            elif event.button == "START":
                canvas.itemconfig(controller.start_button, fill="")

            elif event.button == "DPAD_LEFT":
                canvas.itemconfig(controller.dpad_left, fill="")
            elif event.button == "DPAD_RIGHT":
                canvas.itemconfig(controller.dpad_right, fill="")
            elif event.button == "DPAD_UP":
                canvas.itemconfig(controller.dpad_up, fill="")
            elif event.button == "DPAD_DOWN":
                canvas.itemconfig(controller.dpad_down, fill="")

            elif event.button == "A":
                canvas.itemconfig(controller.A_button, fill="")
                action_move_stop()

            elif event.button == "B":
                canvas.itemconfig(controller.B_button, fill="")

            elif event.button == "Y":
                canvas.itemconfig(controller.Y_button, fill="")
                
                action_special_test_end()
                
            elif event.button == "X":
                canvas.itemconfig(controller.X_button, fill="")


    try:          
        root.update()
    except tk.TclError:
        break

