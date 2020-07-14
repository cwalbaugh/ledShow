#!/usr/bin/env python3
print("Running Show")

import board
from time import sleep
import neopixel
pixels = neopixel.NeoPixel(board.D18, 300)


print("select show:\n")
print("1:show one\n")

show = input("Please enter a show number:\n")
show = int(show)

if show == 1:
    print("running show 1")
    pixels[0] = (255, 0, 0)
    sleep(10)
    pixels[0] = (0, 0, 0)

    for x in range(0, 9):
        pixels[x] = (255, 0, 0)
        sleep(1)

if show == 2:
    pixels.fill((0, 0, 0))
    
    
