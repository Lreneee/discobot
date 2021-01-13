import neopixel

strip = neopixel.Adafruit_NeoPixel(30, 18)
strip.begin()

strip.fill((255, 0, 0))
strip.show()
