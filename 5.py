#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/def/peak.html

import urllib.request as urllib
import pickle

response = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
text = response.read()

pickledBanner = pickle.loads(text)
# print(string_pickle)
with open('solution_5', 'w+') as f:
  for arr in pickledBanner:
    for tup in arr:
      x = tup[0]
      y = tup[1]
      f.write(x*y)
    f.write('\n')