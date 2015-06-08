#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

im = Image.open('/home/samuel/Descargas/oxygen.png')
im_bytes = im.tobytes()
# print(im_bytes)
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
numbers = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for n in numbers:
  print(chr(n), end='')
print()

# not done parsing all the bytes, just looking the output and searching for something