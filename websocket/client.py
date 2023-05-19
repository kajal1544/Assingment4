import asyncio
import websockets


# Define the client handler
async def client():
    # Connect to the WebSocket server
    async with websockets.connect('ws://localhost:8765') as websocket:
        # Send messages to the server
        while True:
            message = input("Enter message (or 'exit' to quit): ")
            if message == 'exit':
                break

            await websocket.send(message)
            print("Sent message: " + message)

            # Receive the echoed message from the server
            response = await websocket.recv()
            print("Received message: " + response)


# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(client())
