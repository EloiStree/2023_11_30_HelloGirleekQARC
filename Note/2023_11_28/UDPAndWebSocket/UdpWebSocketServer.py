import asyncio
import socket
import websockets
from stringtoaction import process_message

password = "AB01"

UDP_IP = "127.0.0.1"
UDP_PORT_UDP = 8081
UDP_PORT_WS = 8079

def message_to_action_filter(message):
    if not message.startswith(password):
        return
    message_to_action(message[len(password):])
    
def message_to_action(message):
    print(f"ZZZ to second file: {message}")

async def websocket_handler(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received from WebSocket: {message}")
        send_to_second_file(message)

def send_to_second_file(message):
    # Here you can implement the logic to send the message to the second Python file.
    # For simplicity, let's just print the message for now.
    print(f"Sending to second file: {message}")
    message_to_action(message)

async def udp_listener():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((UDP_IP, UDP_PORT_UDP))

    while True:
        data, addr = udp_socket.recvfrom(1024)
        message = data.decode('utf-8')
        print(f"Received from UDP: {message}")
        send_to_second_file(message)

if __name__ == "__main__":
    # Create and run the event loop explicitly
    loop = asyncio.get_event_loop()
    
    udp_task = asyncio.ensure_future(udp_listener())
    websocket_task = websockets.serve(websocket_handler, "127.0.0.1", UDP_PORT_WS)

    # Run the tasks within the event loop
    loop.run_until_complete(asyncio.gather(udp_task, websocket_task))
    loop.run_forever()
