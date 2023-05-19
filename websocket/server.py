import asyncio
import websockets


# Define the server handler
async def server(websocket, path):
    # Receive messages from the client
    async for message in websocket:
        print("Received message: " + message)

        # Echo the received message back to the client
        await websocket.send(message)
        print("Sent message: " + message)


# Start the WebSocket server
start_server = websockets.serve(server, "localhost", 8765)

# Run the server until it's closed
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
