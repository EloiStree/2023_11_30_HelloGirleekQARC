import vgamepad as vg
import time

'''
https://pypi.org/project/vgamepad/
XUSB_GAMEPAD_DPAD_UP = 0x0001
XUSB_GAMEPAD_DPAD_DOWN = 0x0002
XUSB_GAMEPAD_DPAD_LEFT = 0x0004
XUSB_GAMEPAD_DPAD_RIGHT = 0x0008
XUSB_GAMEPAD_START = 0x0010
XUSB_GAMEPAD_BACK = 0x0020
XUSB_GAMEPAD_LEFT_THUMB = 0x0040
XUSB_GAMEPAD_RIGHT_THUMB = 0x0080
XUSB_GAMEPAD_LEFT_SHOULDER = 0x0100
XUSB_GAMEPAD_RIGHT_SHOULDER = 0x0200
XUSB_GAMEPAD_GUIDE = 0x0400
XUSB_GAMEPAD_A = 0x1000
XUSB_GAMEPAD_B = 0x2000
XUSB_GAMEPAD_X = 0x4000
XUSB_GAMEPAD_Y = 0x8000
    '''


def pusha(gamepadref):
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

def simulate_xbox_input():
    gamepad1 = vg.VX360Gamepad()
    gamepad2 = vg.VX360Gamepad()
    gamepad3 = vg.VX360Gamepad()
    gamepad4 = vg.VX360Gamepad()
    gamepad5 = vg.VX360Gamepad()

    try:
        while True:
            pusha(gamepad1);
            pusha(gamepad2);
            pusha(gamepad3);
            pusha(gamepad4);
            pusha(gamepad5);
           

    except KeyboardInterrupt:
        pass
    finally:
        gamepad.reset()
        gamepad.update()
        gamepad2.reset()
        gamepad2.update()

if __name__ == "__main__":
    simulate_xbox_input()
