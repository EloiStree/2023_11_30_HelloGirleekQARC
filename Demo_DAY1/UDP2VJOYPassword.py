import os
import socket
import pyvjoy
import time
import traceback

use_print=False

HID_USAGE_X    = 0x30
HID_USAGE_Y    = 0x31
HID_USAGE_Z    = 0x32
HID_USAGE_RX   = 0x33
HID_USAGE_RY   = 0x34
HID_USAGE_RZ   = 0x35
HID_USAGE_SL0  = 0x36
HID_USAGE_SL1  = 0x37

UDP_IP = "0.0.0.0"  
UDP_PORT = 2520    

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


num_devices = 16

vjoy_devices = [None] * num_devices

for i in range(num_devices):
    try:
        vjoy_devices[i] = pyvjoy.VJoyDevice(i+1)
        if use_print:
            print(f"Created VJoyDevice with ID {i+1}")
    except Exception as e:
        if use_print:
            print(f"Failed to create VJoyDevice with ID {i+1}")

        
mode_literal=True #%
mode_doublechar=False #~

angles = [0, 45, 90, 135, 180, 225, 270, 315]
# Mapping directions to angles (in degrees) for a typical POV hat switch
directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
def set_direction_pov(vjoy_device,index, direction):
    # Mapping angles to directions
    angle_mapping = {"N": 0,
                     "NE": 45,
                     "E": 90,
                     "SE": 135,
                     "S": 180,
                     "SW": 225,
                     "SO": 225,
                     "O": 270,
                     "WN": 315,
                     "ON": 315,
                     "EN": 45,
                     "ES": 135,
                     "WS": 225,
                     "OS": 225,
                     "WN": 315,
                     "ON": 315,}

    # Setting the POV hat switch based on the specified direction
    vjoy_device.set_disc_pov(index, angle_mapping[direction])


def password_to_index(password, password_array):
    # Ensure the password is not empty
    if not password:
        return -1

    # Find the index of the password in the array
    try:
        index = password_array.index(password)
        return index
    except ValueError:
        return -1

# Example usage:
passwords = [
    "password1",
    "password2",
    "password3",
    "password4",
    "password5",
    "password6",
    "password7",
    "password8",
    "password9",
    "password10",
    "password11",
    "password12",
    "password13",
    "password14",
    "password15",
    "password16",
    ]


use_file_password=False
if use_file_password and os.path.exists('passwords.txt'):
    # Open and read the file
    with open('passwords.txt', 'r') as file:
        # Read lines from the file and remove newline characters
        passwords = [line.strip() for line in file]
    # Print the imported passwords
    print(passwords)


def reset_joystick_to_default(joystick_device):
    # Set all axes to their default positions (assuming the neutral position is 32767 for a 16-bit axis)
    for axis in range(pyvjoy.HID_USAGE_X, pyvjoy.HID_USAGE_POV):
        joystick_device.set_axis(axis, 32767)

    # Set all buttons to their default positions (assuming they are not pressed)
    for button in range(1, joystick_device.get_button_number() + 1):
        joystick_device.set_button(button, 0)


def manage_command_line(command_line):

    command_line= command_line.replace("\r", "").replace("\n", "").replace("\x00", "")
    if use_print:
        print("CMD R "+command_line)
    joystick_index=0
    if mode_literal:
        #1|A|1|0.999 set the Axis to 1
        #1|A|1|-0.998 set the Axis to -0.998
        #1|B|1 enable button at index 1
        #1|b|13 disable b at index 13
        joystick_data = command_line.strip()
        tokens= joystick_data.split('|')
        lenght_data = len(tokens)

        
        if lenght_data > 1:

            givenPassword=tokens[0]
            joystick_index= password_to_index(givenPassword, passwords)
            
            if joystick_index<0 or joystick_index>15:
                print(f"Failed: {givenPassword}")
                return

            if len(tokens)==4:
                print(f"Succeed: {joystick_index}{tokens[1]}{tokens[2]}{tokens[3]}")
            if len(tokens)==3:
                print(f"Succeed: {joystick_index}{tokens[1]}{tokens[2]}")

            try:
                if vjoy_devices[joystick_index] != None:
                    

"""                    
                    if lenght_data == 2:
                        if tokens[1]=='R' or tokens[1]=='r':
                            reset_joystick_to_default(vjoy_devices[joystick_index])
                        if tokens[1].upper()=='RESET':
                            for item in vjoy_devices:
                                reset_joystick_to_default(item)
"""

                        
                    if lenght_data == 3:
                        
                        if tokens[1]=='B' or tokens[1]=='b':
                            set_bool_active = tokens[1]=='B'
                            
                            button_index = int(tokens[2].strip())
                            vjoy_devices[joystick_index].set_button(button_index, set_bool_active if 1 else 0 )




                    if lenght_data == 4:

                        if tokens[1].lower()=='P':
                            index=int(tokens[2])
                            set_direction_pov(vjoy_devices[joystick_index],index, tokens[3].strip().upper())
                            
                        
                        if tokens[1]=='A' or tokens[1]=='a':
                            
                            try:
                                value = int(((float(tokens[3])+1.0) * 0.5) * 32767.0)
                                label = tokens[2].strip().lower()
                        
                                if   label=="x":
                                    vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_X, value)
                                elif label=="y":
                                    vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_Y, value)
                                elif label=="z":
                                    vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_Z, value)
                                elif  label=="rx":
                                    vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_RX, value)
                                elif  label=="ry":
                                    vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_RY, value)
                                elif  label=="rz":
                                    vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_RZ, value)
                                elif  label=="sl0":
                                    vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_SL0, value)
                                elif  label=="sl1":
                                    vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_SL1, value)
                                else:
                                    
                                    index=int(tokens[2])
                                    if index==0:
                                        vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_X, value)
                                    elif index==1:
                                        vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_Y, value)
                                    elif index==2:
                                        vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_Z, value)
                                    elif index==3:
                                        vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_RX, value)
                                    elif index==4:
                                        vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_RY, value)
                                    elif index==5:
                                        vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_RZ, value)
                                    elif index==6:
                                        vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_SL0, value)
                                    elif index==7:
                                        vjoy_devices[joystick_index].set_axis(pyvjoy.HID_USAGE_SL1, value)
                                    
                            except pyvjoy.vJoyException as e:
                                
                                if use_print:
                                    print(f"vJoyException: {e}")
                           
            except Exception as e:
                # Handle other exceptions
                print(f"An error occurred: {e}")    
                                
    
    if use_print:                        
        print("CMD "+command_line)
                            
def manage_command_line_bytes(command_line_bytes):
    manage_command_line(command_line_bytes.decode('utf-8'))
                    


print("Hello vJoy")
time_between_test=0.1
make_command_test=True
try:
    while True:
        if make_command_test:
            time.sleep(time_between_test)
            manage_command_line("password3|B|10")
            manage_command_line("password3|B|11")
            manage_command_line("password3|B|12")
            manage_command_line("password3|A|0|-1")
            manage_command_line("password3|H|up")
            time.sleep(time_between_test)
            manage_command_line("password16|B|10")
            manage_command_line("password16|B|11")
            manage_command_line("password16|B|12")
            manage_command_line("password16|A|0|-1")
            manage_command_line("password16|H|up")
            manage_command_line("password1|P|1|N")
            time.sleep(0.5)
            manage_command_line("password1|P|2|NE")
            time.sleep(0.5)
            manage_command_line("password1|P|3|SW")
            time.sleep(0.5)
            manage_command_line("password1|P|4|W")
            time.sleep(0.5)
            manage_command_line("2|b|1")
            manage_command_line("2|A|1|0.5")
            manage_command_line("2|H|r")
            time.sleep(time_between_test)
            manage_command_line("password2|B|20")
            manage_command_line("password2|A|2|-1")
            manage_command_line("password2|H|z")
            time.sleep(time_between_test)
            manage_command_line("password1|B|24")
            manage_command_line("password1|A|3|1")
            time.sleep(time_between_test)
            manage_command_line("2|B|1")
            manage_command_line("1|A|4|-0.5")
            time.sleep(time_between_test)
            manage_command_line("2|b|1")
            manage_command_line("1|A|5|0.5")
            time.sleep(time_between_test)
            manage_command_line("2|B|2")
            manage_command_line("1|A|6|-0.5")
            time.sleep(time_between_test)
            manage_command_line("2|b|2")
            manage_command_line("1|A|7|0.5")
        data, addr = sock.recvfrom(64)     
        manage_command_line_bytes(data)
        

except KeyboardInterrupt:
    pass

finally:
    # Release the vJoy device and close the socket on program exit
    
    #vj.reset()
    sock.close()

