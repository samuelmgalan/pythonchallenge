#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/def/map.html

letters = "abcdefghijklmnopqrstuvwxyzab"
clause = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
clause2 = "map";

res = ""
for l in clause2:
  if l == " " or l == "." or l == "(" or l == ")" or l == "'":
    res += l
  else:
    res += letters[letters.find(l)+2]
print(res)

"""
They recommend using string.maketrans(). Should be like this:

  maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
"""