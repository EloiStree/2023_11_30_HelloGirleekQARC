# SOURCE: https://chat.openai.com/c/6bb9866b-dee9-4880-9a40-dc151ccd5a9a
import socket
import keyboard
import threading

# Configuration
UDP_SERVER_ADDRESS = 'localhost'
UDP_SERVER_PORT = 4501
FILTER_STRING = "PP"  # Chaîne pour filtrer les messages UDP

# Fonction pour envoyer un message UDP
def send_udp_message(message):
    print ("Sent:"+message)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.sendto(message.encode('utf-8'), (UDP_SERVER_ADDRESS, UDP_SERVER_PORT))

# Fonction pour envoyer un message d'entrée (ex: J1, J2, etc.)
def send_input_message(input_key, is_key_down):
    
    if is_key_down:
        input_key = input_key.upper()
    else:
        input_key = input_key.lower()
    send_udp_message(f"{FILTER_STRING}{input_key}")

# Fonction de callback pour le hook clavier
def on_key_event(keyboard_event):
    if keyboard_event.event_type in [keyboard.KEY_DOWN, keyboard.KEY_UP]:
        if keyboard_event.name == '7':
            send_input_message("B2", keyboard_event.event_type == keyboard.KEY_DOWN)
        elif keyboard_event.name == '9':
            send_input_message("B3", keyboard_event.event_type == keyboard.KEY_DOWN)
        elif keyboard_event.name == '4':
            send_input_message("B4", keyboard_event.event_type == keyboard.KEY_DOWN)
        elif keyboard_event.name == '6':
            send_input_message("B5", keyboard_event.event_type == keyboard.KEY_DOWN)

# Afficher toutes les adresses IP locales au démarrage
def display_local_ips():
    host_name = socket.gethostname()
    local_ips = socket.gethostbyname_ex(host_name)[2]

    print("Local IP addresses:")
    for ip in local_ips:
        print(f"- {ip}")

# Exemples d'envoi de messages UDP
if __name__ == "__main__":
    # Afficher les adresses IP locales au démarrage
    display_local_ips()

    # Configurer le hook clavier en tant que thread pour fonctionner en arrière-plan
    keyboard.hook(on_key_event)

    # Maintenir le script en cours d'exécution
    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        pass
