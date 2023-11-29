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
