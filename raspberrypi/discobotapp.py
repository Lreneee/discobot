import asyncio
import websockets
import time
import argparse

import dataqueue

music_data = []

def fillMusicData(musicArray):
    global music_data
    music_data = musicArray

async def receive(websocket, path):
    global music_data 
   # ontvangen van data van de app
   # payload is een ontvangen string
    payload = await websocket.recv()
    if payload == 'p':
        print("Irene")
    elif payload == 'b':
        print("Blalbal")
    elif payload == 'd':
        await websocket.send(str(music_data))
# starten van de async loop, gebeurt nu in main
# start_server = websockets.serve(hello, "192.168.0.110", 8765)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

def startAppBackend():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true',
                        help='clear the display on exit')
    args = parser.parse_args()
 
    start_server = websockets.serve(receive, "192.168.0.110", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    

if __name__ == '__main__':
    startAppBackend()
    
