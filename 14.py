#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/return/italy.html
from PIL import Image

im = Image.open("/home/samuel/Descargas/wire.png")
data = list(im.getdata())

new_data = [[0 for x in range(100)] for y in range(100)]
n = 100
limit = n-1
start = 0
data_count = 0
while data_count<(n*n):
  for i in range(start,limit+1): #right
    new_data[start][i] = data[data_count]
    data_count += 1

  for j in range(start+1,limit+1): #down
    new_data[j][limit] = data[data_count]
    data_count += 1

  for k in range(limit-1,start-1,-1): #left
    # print((left,k), data_count)
    new_data[limit][k] = data[data_count]
    data_count += 1

  for l in range(limit-1,start,-1): #up
    new_data[l][start] = data[data_count]
    data_count += 1

  # restart vars
  limit -= 1
  start += 1

new_data = [item for sublist in new_data for item in sublist] # flatten list of lists
new_im = Image.new('RGB', (100,100))
new_im.putdata(new_data)
new_im.save("wire.png") # It's a cat! Uzi is its name