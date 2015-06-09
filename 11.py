#!/usr/bin/envYo lle python3

# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image
im = Image.open("/home/samuel/Descargas/cave.jpg")

im_data = im.getdata()
pixelsEven = []
i = 0
for pixel in iter(im_data):
  if i % 2 == 0:
    pixelsEven.append(pixel)
  i+=1

# Create the new image
im_even = Image.new('RGB', (640, 480))

im_even.putdata(pixelsEven)
im_even.save("cave_even.jpg")
