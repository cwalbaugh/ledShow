#!/usr/bin/env python3
print("Running Show")

import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)


print("select show:\n")
print("1:show one\n")

show = input("Please enter a string:\n")

if show == "1"
    print("running show 1")
    pixels[0] = (255, 0, 0)
    sleep(10)
    pixels[0] = (0, 0, 0)

    for x in range(0, 9):
        pixels[x] = (255, 0, 0)
        sleep(1)
    
    
