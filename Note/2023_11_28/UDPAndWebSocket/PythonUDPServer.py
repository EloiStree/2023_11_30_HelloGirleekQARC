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
