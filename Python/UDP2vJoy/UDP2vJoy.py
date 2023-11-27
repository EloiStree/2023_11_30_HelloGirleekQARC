
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
            try:
                joystick_index= int(tokens[0])-1
            except KeyboardInterrupt:
                return
            if joystick_index<0 or joystick_index>15:
                return
            
            if vjoy_devices[joystick_index] != None:
                
                
                if lenght_data == 3:
                    
                    if tokens[1]=='B' or tokens[1]=='b':
                        set_bool_active = tokens[1]=='B'
                        
                        button_index = int(tokens[2].strip())
                        vjoy_devices[joystick_index].set_button(button_index, set_bool_active if 1 else 0 )

                if lenght_data == 4:
                    
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
                       
                            
    
    if use_print:                        
        print("CMD "+command_line)
                            
def manage_command_line_bytes(command_line_bytes):
    manage_command_line(command_line_bytes.decode('utf-8'))
                    


print("Hello vJoy")
time_between_test=0.1
make_command_test=False
try:
    while True:
        if make_command_test:
            time.sleep(time_between_test)
            manage_command_line("1|B|1")
            manage_command_line("1|A|0|-0.5")
            manage_command_line("1|H|up")
            time.sleep(time_between_test)
            manage_command_line("1|b|1")
            manage_command_line("1|A|1|0.5")
            manage_command_line("1|H|r")
            time.sleep(time_between_test)
            manage_command_line("1|B|2")
            manage_command_line("1|A|2|-0.5")
            manage_command_line("1|H|z")
            time.sleep(time_between_test)
            manage_command_line("1|b|2")
            manage_command_line("1|A|3|0.5")
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
