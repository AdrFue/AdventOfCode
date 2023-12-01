## Teil 1 ##

import os 
dir = os.path.dirname(os.path.realpath(__file__))

with open(dir + "/input.txt", "r") as f:
    for line in f:
      code = line.strip()


for i in range(len(code)):
  curList = code[i:i+4]
  if len(curList) == len(set(curList)):
    print(i+4)
    break


## Teil 2 ##

for i in range(len(code)):
  curList = code[i:i+14]
  if len(curList) == len(set(curList)):
    print(i+14)
    break
