import ctypes
import time

# Constants for SendMessage
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

# Virtual key codes
VK_X = 0x58
VK_LEFT = 0x25
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28
VK_Z = 0x5A
VK_R = 0x52

timebetweenaction=0.1
timepress=0.1

# Find the window by its title
def find_window(title):
    return ctypes.windll.user32.FindWindowW(None, title)

# Send key press using SendMessage
def send_key(hwnd, key_code):
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, key_code, 0)
    time.sleep(timepress)  # Optional delay between keydown and keyup
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, key_code, 0)

if __name__ == "__main__":
    # Replace "Your Window Title" with the title of the window you want to send keys to
    window_title = "10 Second Ninja"
    hwnd = find_window(window_title)

    if hwnd:
        while True:
            send_key(hwnd, VK_X)
            time.sleep(timebetweenaction)
            send_key(hwnd, VK_RIGHT)
            time.sleep(timebetweenaction)
            send_key(hwnd, VK_UP)
            time.sleep(timebetweenaction)
            send_key(hwnd, VK_DOWN)
            time.sleep(timebetweenaction)
            send_key(hwnd, VK_Z)
            time.sleep(timebetweenaction)
            send_key(hwnd, VK_R)
        
    else:
        print(f"Window with title '{window_title}' not found.")
