#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/return/bull.html
def length_i(integer):
  return len(str(integer))

def calculate_next(actual):
  count = 1
  num_str = str(actual)
  res_str = ""
  for i in range(1,length_i(actual)):
    if num_str[i] == num_str[i-1]:
      count+=1
      continue
    else:
      res_str+=str(count)+num_str[i-1]
      count = 1

  if res_str != "":
    return int(res_str+str(count)+str(num_str[-1]))
  else:
    return int(str(count)+str(num_str[1]))


def long_list(length):
  l = [1, 11]
  for num in range(2, length):
    l.append(calculate_next(l[num-1]))
  return l

my_list = long_list(31)
print(len(str(my_list[30]))) 
# [1, 11, 21, 1211, 111221,...] 
# explanation: 1, one 1, two 1s, one 2 one 1, one 1 one 2 two 1s, ...