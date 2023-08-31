import asyncio 

import websockets

async def send_msg():
    url = "ws://localhost:6666"
    
    
    async with websockets.connect(url) as websocket:
        name = input("What is your name: ")
            
        await websocket.send(name)  
            
        print(f'Client sent: {name}')
        greeting = await websocket.recv() 
            
        print(f'Client received: {greeting}')
    
        
if __name__ == "__main__":

    asyncio.run(send_msg())

