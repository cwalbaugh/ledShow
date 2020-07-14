import board
import neopixel
#pixels = neopixel.NeoPixel(board.D18, 300, brightness=0.2, auto_write=True, pixel_order=neopixel.RGB)
#pixels = neopixel.NeoPixel(board.D18, 300, brightness=0.01)
pixels = neopixel.NeoPixel(board.D18, 300)

#pixels[0] = (0, 0, 0)
pixels[0] = (255, 255, 255)
#pixels.fill((238, 130, 238))
#pixels.fill((255, 255, 255))
#pixels.fill((255, 0, 0))
