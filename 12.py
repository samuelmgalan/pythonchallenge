#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/return/evil.html

# evil1.jpg, evil2.jpg, evil3.jpg, evil4.jpg 
# the last one is not an image
# the file contains this: QmVydCBpcyBldmlsISBnbyBiYWNrIQo= (text encoded in base64). Decoded: Bert is evil! go back! (??)

#evil2.jpg says: "not jpg _.gfx". Changing url to /evil2.gfx downloads a new file

f = open("/home/samuel/Descargas/evil2.gfx", "rb").read()
# print(f[0:60:5])
# print(f[1:60:5])
# print(f[2:60:5])
# print(f[3:60:5])
# print(f[4:60:5])
# It looks like there are 5 different files inside the .gfx: 2 JPEGs, 2 PNGs and 1 GIF
types = ['jpg' , 'png', 'gif', 'png', 'jpg']
for i in range(5):
  open('evil2-%d.%s' % (i, types[i]), 'wb').write(f[i::5])

# disproportional