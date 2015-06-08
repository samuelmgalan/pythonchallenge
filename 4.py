#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request as urllib

response = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")
nothing = int(response.read().split()[5])

for i in range(200):
  url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(nothing)
  print(url)
  response = urllib.urlopen(url)
  phrase = response.read().split()
  print(phrase)
  nothing = int(phrase[len(phrase)-1])