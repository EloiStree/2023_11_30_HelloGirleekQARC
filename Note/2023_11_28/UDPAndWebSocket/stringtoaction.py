# second_file.py
import ctypes
from pynput.keyboard import Key, Controller
#pip install pywin32
# https://nitratine.net/blog/post/simulate-keypresses-in-python/
import vgamepad as vg
import pyvjoy
import time
import socket
password= "001"

#'numpad 0'
keyboardLF=0x61
keyboardRF=0x62
keyboardLB=0x63
keyboardRB=0x64
vJoyLF = 2
vJoyRF = 3
vJoyLB = 4
vJoyRF = 5
gamepad1 = vg.VX360Gamepad()
gamepad2 = vg.VX360Gamepad()
keyboard = Controller()

#VK_NUMPAD1 = 0x61
#VK_NUMPAD2 = 0x62
#VK_NUMPAD3 = 0x63
#VK_NUMPAD4 = 0x64
#VK_1 = 0x31
#VK_2 = 0x32
#VK_3 = 0x33
#VK_4 = 0x34
# Constants for SendMessage
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

VK_X = 0x58
VK_LEFT = 0x25
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28
VK_Z = 0x5A
VK_R = 0x52
VK_1 = 0x31
VK_2 = 0x32
VK_1 = 0x67
VK_2 = 0x69


window_title="10 Second Ninja"
#window_title="HelloQARC"

NUM_DEVICES_START = 0
NUM_DEVICES = 6
vjoy_devices = [pyvjoy.VJoyDevice(i) for i in range(1+NUM_DEVICES_START, NUM_DEVICES+NUM_DEVICES_START + 1)]




udp_ip = "127.0.0.1"
udp_port = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

hwnd=0


# Find the window by its title
def find_window(title):
    return ctypes.windll.user32.FindWindowW(None, title)

# Send key press using SendMessage
def press_key( key_code):
    global hwnd
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, key_code, 0)
    
def release_key( key_code):
    global hwnd
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, key_code, 0)
    # Send key press using SendMessage
def press_keyh( hwnd,key_code):
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, key_code, 0)
    
def release_keyh(hwnd, key_code):
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, key_code, 0)

def send_key(hwnd, key_code):
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, key_code, 0)
    time.sleep(1)  # Optional delay between keydown and keyup
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, key_code, 0)

def ini_message_to_action():
    global hwnd
    print(f"Start secondary file")
    global gamepad1 
    global gamepad2
    gamepad1 = vg.VX360Gamepad()
    gamepad2 = vg.VX360Gamepad()
    # Start the vJoy update threads for each device
    keyboard = Controller()
    hwnd = find_window(window_title)
    if hwnd:
        print(f"Window with title '{window_title}'  found.")
    else:
        print(f"Window with title '{window_title}' not found.")
        
    
    

def update_vjoy(device_index, button, isTrue):
    vjoy_devices[device_index].set_button(button, isTrue)

def update_vjoy_all( button, isTrue):
    for element in vjoy_devices:
        element.set_button(button, isTrue)


def gamepadrefdemo(gamepadref):
    gamepadref.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)  # press the left hat button
    gamepadref.update() 
    time.sleep(0.1)
    gamepadref.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)  # press the left hat button
    gamepadref.update() 
    time.sleep(0.5)
    gamepadref.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)  # release the A button
    gamepadref.update()  
    time.sleep(0.1)
    gamepadref.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)  # release the A button
    gamepadref.update()  
    time.sleep(0.1)
def gamepadrefzero(gamepadref):
    gamepadref.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)  # press the left hat button
    gamepadref.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)  # press the left hat button
    gamepadref.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button
    gamepadref.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)  # release the A button
    gamepadref.update()
def gamepadrefone(gamepadref):
    gamepadref.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)  # press the left hat button
    gamepadref.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)  # press the left hat button
    gamepadref.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button
    gamepadref.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)  # release the A button
    gamepadref.update()
def gamepadrefforward(gamepadref):
    gamepadref.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)  # press the left hat button
    gamepadref.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)  # press the left hat button
    gamepadref.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button
    gamepadref.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)  # release the A button
    gamepadref.update()  
    

def message_to_action(message):
    message= message.strip()
    if len(message)!=2:
        print(f"Received (not double char): {message}")
        return;
    c0=message[0]
    c1=message[1]

    print(f"C0:{c0} C1:{c1}")
    # Process the received message as needed
    """
        #Clavier
    if(c0=='K'and c1=='0'):
        print(f"Keyboard Reset")
        release_key(keyboardLF)
        release_key(keyboardLB)
        release_key(keyboardRF)
        release_key(keyboardRB)
        
    if(c0=='K'and c1=='1'):
        print(f"Keyboard LF On")
        
        press_key(keyboardLF)
    if(c0=='K'and c1=='2'):
        print(f"Keyboard RF On")
        press_key(keyboardRF)
        
    if(c0=='K'and c1=='3'):
        print(f"Keyboard LB On")
        press_key(keyboardLB)
        
    if(c0=='K'and c1=='4'):
        print(f"Keyboard RF On")
        press_key(keyboardRB)
        
    if(c0=='k'and c1=='0'):
        print(f"Keyboard Reset")
        release_key(keyboardLF)
        release_key(keyboardLB)
        release_key(keyboardRF)
        release_key(keyboardRB)
        
    if(c0=='k'and c1=='1'):
        print(f"Keyboard LF")
        release_key(keyboardLF)
        send_key(hwnd,VK_R)
        time.sleep(1)
        send_key(hwnd,VK_X)
        
    if(c0=='k'and c1=='2'):
        print(f"Keyboard RF")   
        release_key(keyboardRF)
        
    if(c0=='k'and c1=='3'):
        print(f"Keyboard LB")
        release_key(keyboardLB)
        
    if(c0=='k'and c1=='4'):
        print(f"Keyboard RB")
        release_key(keyboardRB)
      """  

        #XBOX One
    if(c0=='x'and c1=='0'):
        print(f"Xbox1 Reset")
        gamepadrefzero(gamepad1)
    if(c0=='x'and c1=='1'):
        print(f"Xbox1 LF Off")
        gamepadrefone(gamepad1)
    if(c0=='x'and c1=='2'):
        print(f"Xbox1 RF Off")   
        gamepadrefforward(gamepad1)
    if(c0=='x'and c1=='3'):
        print(f"Xbox1 LB Off")
    if(c0=='x'and c1=='4'):
        print(f"Xbox1 RB Off")
    if(c0=='X'and c1=='0'):
        print(f"Xbox1 Reset")
    if(c0=='X'and c1=='1'):
        print(f"Xbox1 LF On")
    if(c0=='X'and c1=='2'):
        print(f"Xbox1 RF On")   
    if(c0=='X'and c1=='3'):
        print(f"Xbox1 LB On")
    if(c0=='X'and c1=='4'):
        print(f"Xbox2 RB On")


            #vJoy One
    if(c0=='V'and c1=='0'):
        print(f"Xbox1 Reset")
    if(c0=='V'and c1=='1'):
        print(f"Xbox1 LF Off")
        update_vjoy_all(vJoyLF,True)
    if(c0=='V'and c1=='2'):
        print(f"Xbox1 RF Off")   
        update_vjoy_all(vJoyRF,True)
    if(c0=='V'and c1=='3'):
        print(f"Xbox1 LB Off")
        update_vjoy_all(vJoyLB,True)
    if(c0=='V'and c1=='4'):
        print(f"Xbox1 RB Off")
        update_vjoy_all(vJoyRB,True)
    if(c0=='v'and c1=='0'):
        print(f"Xbox1 Reset")
    if(c0=='v'and c1=='1'):
        print(f"Xbox1 LF On")
        update_vjoy_all(vJoyLF,False)
    if(c0=='v'and c1=='2'):
        print(f"Xbox1 RF On")   
        update_vjoy_all(vJoyRF,False)
    if(c0=='v'and c1=='3'):
        print(f"Xbox1 LB On")
        update_vjoy_all(vJoyLB,False)
    if(c0=='v'and c1=='4'):
        print(f"Xbox2 RB On")
        update_vjoy_all(vJoyRB,False)



def message_to_action_filter(message):
    if not message.startswith(password):
        print(f"Refused: {message}")
        return
    message_to_action(message[len(password):])
    


def process_message(message):
    #print(f"Processing message: {message}")
    message_to_action_filter(message)
def test_ninja():
    hwnd = find_window("10 Second Ninja")
    for i in range(5):
        time.sleep(0.5)
        send_key(hwnd,VK_R)
        time.sleep(0.5)
        press_key(VK_R)
        time.sleep(0.5)
        release_key(VK_R)
        time.sleep(0.5)
        press_key(VK_X)
        time.sleep(0.5)
        release_key(VK_X)
        time.sleep(0.5)
        send_key(hwnd,VK_X)
        print(f"Ninja ")

def test_hellorc():
    hwnd = find_window("HelloQARC")
    for i in range(5):
        time.sleep(0.5)
        send_key(hwnd,VK_1)
        time.sleep(0.5)
        press_key(VK_1)
        time.sleep(0.5)
        release_key(VK_1)
        time.sleep(0.5)
        press_key(VK_2)
        time.sleep(0.5)
        release_key(VK_2)
        time.sleep(0.5)
        send_key(hwnd,VK_2)
        print(f"RC s")
        release_keyh(hwnd,VK_2)
        release_keyh(hwnd,VK_1)
        time.sleep(2)
        print(f"RC ")
    
if __name__ == "__main__":
    test_hellorc()
    test_ninja()
    
    hwnd = find_window(window_title)
    if hwnd:
        print(f"Window with title '{window_title}'  found.")
    else:
        print(f"Window with title '{window_title}' not found.")
    
    """  
    test_ninja()
    #"""
    ini_message_to_action()
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message: {data.decode('utf-8')} from {addr}")
        process_message(data.decode('utf-8'))
