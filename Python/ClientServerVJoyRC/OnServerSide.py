import socket
import random
from pyvjoy import VJoyDevice
import ctypes

# Variables de configuration
JOYSTICK_ID = 1  # Numéro du joystick VJoy à influencer
BUTTONS_TO_CHANGE = [ 2, 3, 4, 5]  # Liste des boutons à changer aléatoirement
SERVER_PORT = 4501  # Port sur lequel le serveur UDP écoute
CONSOLE_TITLE = "Player Eloi"  # Titre de la console
FILTER_STRING = "PP"  # Chaîne pour filtrer les messages UDP

# Fonction pour changer aléatoirement les boutons VJoy
def randomize_buttons(vjoy_device):
    for button in BUTTONS_TO_CHANGE:
        vjoy_device.set_button(button, random.randint(0, 1))

# Fonction pour traiter le message et changer le bouton correspondant
def process_message(message, vjoy_device):
    if message.startswith("B") and message[1:].isdigit():
        index = int(message[1:])
        if index in BUTTONS_TO_CHANGE:
            vjoy_device.set_button(index, 1)
    elif message.startswith("b") and message[1:].isdigit():
        index = int(message[1:])
        if index in BUTTONS_TO_CHANGE:
            vjoy_device.set_button(index, 0)

# Fonction principale du serveur UDP
def start_udp_server(port=SERVER_PORT):
    host_name = socket.gethostname()
    local_ips = socket.gethostbyname_ex(host_name)[2]

    print("Local IP addresses:")
    for ip in local_ips:
        print(f"- {ip}")
    # Création d'un objet VJoy pour manipuler les boutons
    vjoy_device = VJoyDevice(JOYSTICK_ID)

    # Configuration du serveur UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('localhost', port))

    print(f"Le serveur UDP écoute sur le port {port}...")

    try:
        while True:
            # Attente de la réception de données UDP
            data, _ = udp_socket.recvfrom(1024)

            # Vérification de la chaîne de filtre
            if data.decode('utf-8').startswith(FILTER_STRING):
                # Changer les boutons VJoy aléatoirement
                #randomize_buttons(vjoy_device)
                #print("Boutons VJoy changés")

                # Traitement du message et changement du bouton correspondant
                message = data.decode('utf-8')[len(FILTER_STRING):]
                process_message(message, vjoy_device)
                print(f"Message UDP reçu : {message}")
            else:
                message = data.decode('utf-8')[len(FILTER_STRING):]
                print(f"Message UDP reçu  mais ignoré: {message}")

    finally:
        # Fermer le socket UDP et le dispositif VJoy à la fin
        udp_socket.close()
        vjoy_device.close()

if __name__ == "__main__":
    # Modifier le titre de la console (Windows seulement)
    ctypes.windll.kernel32.SetConsoleTitleW(CONSOLE_TITLE+str(SERVER_PORT))

    # Démarrer le serveur UDP
    start_udp_server()
