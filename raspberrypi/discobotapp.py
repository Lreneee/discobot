import asyncio
import websockets
import time
from rpi_ws281x import *
import argparse

import dataqueue

LED_COUNT = 10
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

music_data = []

def fillMusicData(musicArray):
    global music_data
    music_data = musicArray
    
"""
# Prevent visualization.py from controlling led strip
dataqueue.AppControlOn
# Give control back to visualization.py
dataqueue.AppControlOff()
"""

async def hello(websocket, path):
    # ontvangen van data van de app
    # payload is een ontvangen string
    payload = await websocket.recv()
    if payload == 'p':
        print("Irene")
        colorWipe(strip, Color(255, 0, 0))
    elif payload == 'b':
        colorWipe(strip, Color(0, 255, 0))

# starten van de async loop, gebeurt nu in main
# start_server = websockets.serve(hello, "192.168.0.110", 8765)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def startAppBackend():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true',
                        help='clear the display on exit')
    args = parser.parse_args()

    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
#    colorWipe(strip, Color(255, 0, 0))

    start_server = websockets.serve(hello, "192.168.0.110", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    startAppBackend()
