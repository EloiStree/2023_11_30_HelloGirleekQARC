![image](https://github.com/EloiStree/2023_11_30_HelloGirleekQARC/assets/20149493/4cb8726b-02b7-4b3f-a912-e1d2d40a8f82)

# Participer au Jeu "HelloCarRCUnity" - Instructions

Maintenant que vous avez appris à utiliser Python dans "10 seconds Ninja", je vous invite à participer au jeu de cet atelier.

> Ce jeu est le fil conducteur de cet atelier. Je vous invite à travailler sur le sujet si vous êtes en avance ou lors de vos temps libres.

Sur une clé USB ou sur le Git, vous pouvez trouver une release d'un jeu Unity :  
[HelloCarRCUnity Releases](https://github.com/EloiStree/2023_11_22_HelloCarRCUnity/tags)  
Ainsi que son code source si cela vous intéresse :   
[Code source HelloCarRCUnity](https://github.com/EloiStree/2023_11_22_HelloCarRCUnity)  

L'idée est que le jeu est jouable à 22+ joueurs mais n'est pas un jeu en réseau. Chaque joueur dans le jeu correspond à une entrée qui est hackable en tant que testeur de jeux vidéo.

Pour jouer au jeu, rien de plus simple. Il vous faut simuler des touches de manettes Xbox et de joysticks via vJoy :) Entraînez-vous localement à contrôler les voitures du jeu pour apprendre.

Mais le jeu est une arène composée de deux équipes.

Rouge contre bleu, il vous faut pousser la boule jaune sur la boule du camp adverse pour gagner des points. Le premier à 5 gagne une manche. L'équipe gagnante est la meilleure des 5 manches.

### Comment jouer au jeu ensemble ?

L'écran de jeu est projeté sur l'écran de l'enseignant. Il n'y a donc que deux moyens pour contrôler le jeu : par réseau (UDP, WebSocket, autre proposé) ou par matériel (Arduino, Raspberry Pi Pico, Arcade board).

> Attention, c'est la première version du jeu.
> Et le jeu tourne sur mon ordinateur de travail.
> - Je vous fais confiance pour cette atelier de ne pas m'obliger à tout installer sur une machine virtuelle.
> - Et je vous fais confiance pour ne pas tricher.
> - Le moindre doute de triche ou lecture d'un code qui n'est pas dans ces conditions est égal à une manche perdue.

Plusieurs méthodes.
La principale :
- Créez en équipe un/des scripts Python propres à votre équipe que je ferai tourner sur le PC pendant les matchs.

Les méthodes secondaires :
- Utilisez des codes que je fournis en exemple du cours via UDP ou WebSocket.
  - Ils tourneront sur l'ordinateur projeté sur l'écran.
- Utilisez des macros par UDP que je prépare via UDP sur la suite Open Macro Input.
  - Utiliser JOMI pour le clavier
  - UDP2vJoy pour vJoy
  - XOMI pour les manettes Xbox  
  - Note : Je ne les lance que si un étudiant décide de l'utiliser.
- Utilisez du matériel avec un Arduino ou un Raspberry Pi Pico

Note : J'ai amené du matériel que vous pouvez utiliser sur vos machines
- Joystick d'arcade Chinois  
- Des manettes Xbox
- Des claviers pour doigts
- Pour les experts : Deux Brook avec Arduino + HC06

Pour éviter la triche un minimum sur les exemples de cours, un mot de passe est donné à chaque équipe.

**Important : règles de distribution**

> Les scripts des rouges sont exécutés avant les scripts des bleus pour permettre au rouge d'émuler la Xbox 1 et 2.

Une équipe n'a droit qu'à deux manettes Xbox et 8 joysticks vJoy.

L'équipe rouge a 
- Le contrôleur Xbox 1 et 2
- Les vjoys de 1-8
- L'injection de clavier Alpha 2 3 4 5

L'équipe bleue a 
- Le contrôleur Xbox 3 et 4 (exécuter après le premier script)
- Les vjoys de 9-16
- L'injection de clavier Numpad 2 3 4 5



## UDP & Websocket


Pour pouvoir communiquer avec les scripts qui tournent sur le PC, je vous invite à regarder les deux exemples suivants sur comment générer un serveur UDP ou un serveur WebSocket. Assez simple.

Comment créer un serveur UDP qui écoute les messages entrants.

``` py 

import socket
from stringtoaction import process_message
from stringtoaction import ini_message_to_action

udp_ip = "127.0.0.1"
udp_port = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

ini_message_to_action()
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received message: {data.decode('utf-8')} from {addr}")
    process_message(data.decode('utf-8'))


``` 

Exemple de comment créer un serveur en WebSocket.

``` py

import asyncio
import websockets
from stringtoaction import process_message
from stringtoaction import ini_message_to_action

ws_port = 8079
#pip install asyncio
#pip install websockets

ini_message_to_action()
async def handle_websocket(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received message: {message}")
        # Process the received message as needed
        process_message(message)

start_server = websockets.serve(handle_websocket, "127.0.0.1", ws_port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

```


Exemple de comment faire un code externe à la logique pour recevoir des commandes.
Nom du fichier : `stringtoaction.py`

``` py 

# Add what you need to create at start before using the reste of the code.
def ini_message_to_action():
    print(f"Script start.")


# Here we deall with message that are filter as valide
def message_to_action(message):
    message= message.strip()
    if len(message)!=2:
        print(f"Received as text: {message}")
        return;

    # You can use text but it will slow your script and the wifi
    # A way you can remote control without blocking the bandwidth is by sending just two char q0 k5 Aa Jk li
    # You could use ,; /ç !) but they are less easy to write on a phone keyboard.        
    c0=message[0]
    c1=message[1]

    print(f"C0:{c0} C1:{c1}")
    # Process the received message as needed
    if(c0=='K'and c1=='0'):
        print("Do something")
    else if(c0=='i'and c1=='1'):
        print("Do something else")

# protect your code with a password the message need to start with.
# Not the best but good enough for the workshop
def message_to_action_filter(message):
    if not message.startswith(password):
        print(f"Refused: {message}")
        return
    message_to_action(message[len(password):])
    

# Function that will be call when a message is received from somewhere
def process_message(message):
    #print(f"Processing message: {message}")
    message_to_action_filter(message)

```


Vous pouvez aussi utiliser une méthode plus classique avec un serveur MQTT si vous savez comment configurer un broker.

Code pour se connecter à un serveur Python et écouter tous les messages.


``` py

import paho.mqtt.server as mqtt

# Callback when a client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Callback when a client publishes a message
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload}")

# Set up the MQTT broker
broker_address = "127.0.0.1"  # Change this to your broker's IP address
broker_port = 1883

# Create an MQTT broker instance
mqtt_broker = mqtt.MQTTServer()
mqtt_broker.on_connect = on_connect
mqtt_broker.on_message = on_message

# Start the broker
mqtt_broker.start(broker_address, broker_port)

# Run the loop to keep the server running
mqtt_broker.loop_forever()

```





# UDP 2 vJoy


``` py

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


```