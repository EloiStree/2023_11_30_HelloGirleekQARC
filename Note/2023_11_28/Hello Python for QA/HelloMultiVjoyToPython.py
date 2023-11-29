import pyvjoy
import keyboard
import time
import threading

# Define the number of vJoy devices
NUM_DEVICES = 12

# Create a list to store vJoy devices
vjoy_devices = [pyvjoy.VJoyDevice(i) for i in range(1, NUM_DEVICES + 1)]

# Define the axis ranges (you may need to adjust these based on your vJoy setup)
AXIS_MIN = 0
AXIS_MAX = 32767

BUTTON_2 = 2
BUTTON_3 = 3
BUTTON_4 = 4
BUTTON_5 = 5
keyboardforall_2 = 'u'
keyboardforall_3 = 'o'
keyboardforall_4 = 'j'
keyboardforall_5 = 'l'
keyboardforall_2_state = False
keyboardforall_3_state = False
keyboardforall_4_state = False
keyboardforall_5_state = False

# Define the update interval in seconds
UPDATE_INTERVAL = 0.01


def push_two_button_from_one(what_to_push, previous_state, push_on,push_two):
    state = keyboard.is_pressed(what_to_push)
    if(previous_state != state):
        if state==True:
            keyboard.press(push_on)
            keyboard.press(push_two)
                
        if state==False:
            keyboard.release(push_on)
            keyboard.release(push_two)
    previous_state =state

# Function to update vJoy based on keyboard input
def update_vjoy(device_index):
    while True:
        """
        # Check if the 'W' key is pressed for forward movement
        if keyboard.is_pressed('w'):
            vjoy_devices[device_index].set_axis(pyvjoy.HID_USAGE_Y, AXIS_MAX)
        else:
            vjoy_devices[device_index].set_axis(pyvjoy.HID_USAGE_Y, AXIS_MIN)

        # Check if the 'A' key is pressed for left movement
        if keyboard.is_pressed('a'):
            vjoy_devices[device_index].set_axis(pyvjoy.HID_USAGE_X, AXIS_MIN)
        # Check if the 'D' key is pressed for right movement
        elif keyboard.is_pressed('d'):
            vjoy_devices[device_index].set_axis(pyvjoy.HID_USAGE_X, AXIS_MAX)
        else:
            vjoy_devices[device_index].set_axis(pyvjoy.HID_USAGE_X, AXIS_MIN)
        """
        vjoy_devices[device_index].set_button(BUTTON_2, keyboard.is_pressed(keyboardforall_2))
        vjoy_devices[device_index].set_button(BUTTON_3, keyboard.is_pressed(keyboardforall_3))
        vjoy_devices[device_index].set_button(BUTTON_4, keyboard.is_pressed(keyboardforall_4))
        vjoy_devices[device_index].set_button(BUTTON_5, keyboard.is_pressed(keyboardforall_5))

        # Simuler la pression des touches du pavé numérique
        """
        if device_index==1:
            push_two_button_from_one(keyboardforall_2,keyboardforall_2_state, 'c', '1')
            push_two_button_from_one(keyboardforall_3,keyboardforall_3_state, 'v', '2')
            push_two_button_from_one(keyboardforall_4,keyboardforall_4_state, 'b', '3')
            push_two_button_from_one(keyboardforall_5,keyboardforall_5_state, 'n', '4')
        """

        # Simuler la pression des touches du pavé alphabétique
       

        time.sleep(UPDATE_INTERVAL)

print("Hello vJoy")


# Start the vJoy update threads for each device
update_threads = [threading.Thread(target=update_vjoy, args=(i,)) for i in range(NUM_DEVICES)]
for thread in update_threads:
    thread.start()

tickCount = 0
# Keep the program running
try:
    while True:
        time.sleep(1)
        print("Tic"+str(tickCount))
        tickCount=tickCount + 1
except KeyboardInterrupt:
    # Release all vJoy devices on program exit
    for device in vjoy_devices:
        device.reset()

    for thread in update_threads:
        thread.join()
