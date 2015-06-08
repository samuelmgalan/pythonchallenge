#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/def/channel.html

from pathlib import Path
import zipfile

myzip = zipfile.ZipFile('/home/samuel/Descargas/channel.zip', 'r')
arr = []
for f in myzip.filelist:
  if f.filename != 'readme.txt':
    comments = (f.filename, f.comment.decode("utf-8")) # decode() function used to get rid of the 'b' => b'*'
    arr.append(comments)
mydict = (dict(arr))

# Probably could do this part below with the myzip object, but this was done before the comments part, so I didn't redo it
channel = Path('/home/samuel/Descargas/channel')
nextFile = '90052.txt'
res = ""
for i in range(909):
  with (channel/nextFile).open() as f:
    res += str(mydict[nextFile])
    words = f.read()
    # print(words)
    nextFile = words.split()[-1] + '.txt'

print(res)