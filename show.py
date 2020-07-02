#!/usr/bin/env python3
print("Running Show")

import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)

pixels[0] = (255, 0, 0)
