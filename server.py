import asyncio
import websockets


async def receive_message(websocket):
    name = await websocket.recv() 
    
    print(f'Server Received: {name}') 
    
    greeting = f"Hello {name}"
    
    await websocket.send(greeting) 
    
    print(f'Server sent: {greeting}')
    
    
async def run():
    async with websockets.serve(receive_message, "localhost", 6666):
        await asyncio.Future()
        
if __name__ == "__main__":
    asyncio.run(run())
