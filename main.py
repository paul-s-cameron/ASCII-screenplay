import os
from re import ASCII
import time
from math import ceil, floor

import cursor
import dxcam
from PIL import Image, ImageEnhance

# ASCII_CHARS = [' ', '.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']
# ASCII_CHARS = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']
ASCII_CHARS = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

camera = dxcam.create()
cursor.hide()

def image_to_ascii(image, dimension, fps, brightness=None, contrast=150) -> str:
    width, height = dimension
    height -= 2
    image = Image.fromarray(image)
    if contrast is not None:
        image = ImageEnhance.Contrast(image).enhance(contrast)
    if brightness is not None:
        image = ImageEnhance.Brightness(image).enhance(brightness)
    image = image.resize((width, height))
    image = image.convert('L')
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[ceil(pixel_value / (255 / (len(ASCII_CHARS)-1)))] for pixel_value in initial_pixels]
    pixels = ''.join(new_pixels)
    len_pixels = len(pixels)
    
    for index in range(0, len_pixels, width):
        if index == 0:
            print(f"FPS: {fps}" + pixels[index:index + width][5+len(str(fps)):])
        else: print(pixels[index:index + width])
    print("\033[F"*(height+5))

def capture_screen():
    camera.start(target_fps=30)
    os.system('cls')
    ttlf = time.time()
    while True:
        frame = camera.get_latest_frame()
        if frame is not None:
            fps = int(1.0 / (time.time() - ttlf))
            ttlf = time.time()
            image_to_ascii(frame, os.get_terminal_size(), fps, None, 100)

if __name__ == '__main__':
    capture_screen()