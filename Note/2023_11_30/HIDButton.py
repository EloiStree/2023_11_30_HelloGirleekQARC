from pywinusb import hid
import threading

# Global variable to store the previous data
previous_data = None

def joystick_callback(data):
    global previous_data

    # Compare with previous data
    if data != previous_data:
        print("Received data from joystick:", data)
        previous_data = data

def hid_thread():
    hid.core.HidThread.process()

def main():
    # Define the Vendor ID (vID) and Product ID (pID) for the Generic USB Joystick
    target_vid = 0x0079
    target_pid = 0x0006

    # Find the Generic USB Joystick among all HID devices based on vID and pID
    joystick = None
    all_hids = hid.find_all_hid_devices()
    for device in all_hids:
        if device.vendor_id == target_vid and device.product_id == target_pid:
            joystick = device
            break

    if joystick is not None:
        print(f"Found Generic USB Joystick (vID={target_vid}, pID={target_pid}):", joystick.product_name)

        try:
            joystick.open()
            joystick.set_raw_data_handler(joystick_callback)

            print("Listening for events. Press Ctrl+C to exit.")
            
            # Start HID thread
            hid_thread = threading.Thread(target=hid_thread)
            hid_thread.daemon = True
            hid_thread.start()
            
            # Start Joystick thread
            joystick_thread = threading.Thread(target=joystick.hid_thread_proc)
            joystick_thread.daemon = True
            joystick_thread.start()
            
            # Keep the program running until interrupted
            hid_thread.join()
            joystick_thread.join()

        except Exception as e:
            print("Error:", e)
            if joystick.is_opened():
                joystick.close()

    else:
        print(f"Generic USB Joystick (vID={target_vid}, pID={target_pid}) not found.")

if __name__ == "__main__":
    main()
