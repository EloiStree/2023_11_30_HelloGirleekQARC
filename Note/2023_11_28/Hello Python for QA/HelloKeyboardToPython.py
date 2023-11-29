import pyvjoy
import keyboard
import time

# Define the vJoy device
vjoy_device = pyvjoy.VJoyDevice(1)

# Define the axis ranges (you may need to adjust these based on your vJoy setup)
AXIS_MIN = 0
AXIS_MAX = 32767

# Define the update interval in seconds
UPDATE_INTERVAL = 0.01

# Function to update vJoy based on keyboard input
def update_vjoy():
    while True:
        # Check if the 'W' key is pressed for forward movement
        if keyboard.is_pressed('w'):
            vjoy_device.set_axis(pyvjoy.HID_USAGE_Y, AXIS_MAX)
        else:
            vjoy_device.set_axis(pyvjoy.HID_USAGE_Y, AXIS_MIN)

        # Check if the 'A' key is pressed for left movement
        if keyboard.is_pressed('a'):
            vjoy_device.set_axis(pyvjoy.HID_USAGE_X, AXIS_MIN)
        # Check if the 'D' key is pressed for right movement
        elif keyboard.is_pressed('d'):
            vjoy_device.set_axis(pyvjoy.HID_USAGE_X, AXIS_MAX)
        else:
            vjoy_device.set_axis(pyvjoy.HID_USAGE_X, AXIS_MIN)

        time.sleep(UPDATE_INTERVAL)

# Start the vJoy update in a separate thread
update_thread = threading.Thread(target=update_vjoy)
update_thread.start()

# Keep the program running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Release the vJoy device on program exit
    vjoy_device.reset()
    update_thread.join()
