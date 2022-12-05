## Teil 1 ##

import os 
dir = os.path.dirname(os.path.realpath(__file__))
inputs = []

with open(dir + "/input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip())

# print(inputs)

values = []
for input in inputs:
  curLine = []
  curLine.append(input[:len(input)//2])
  curLine.append(input[len(input)//2:])
  values.append(curLine)

sumPrios = 0

for value in values:
  # print(value[0], value[1])
  intersect = list(set(value[0]) & set(value[1]))
  # print(a)
  for c in intersect:
    ascii = ord(c)
    if ascii in range(ord("a"), ord("z") + 1):
      sumPrios += ascii - 96
    elif ascii in range(ord("A"), ord("Z") + 1):
      sumPrios += ascii - 38

print(sumPrios) 


## Teil 2 ##

sumBadges = 0

for i in range(0, len(inputs), 3):
  # print(input)
  curInput = []
  curInput.append(inputs[i])
  curInput.append(inputs[i+1])
  curInput.append(inputs[i+2])
  # print(curInput)
  intersects = list(set(curInput[0]) & set(curInput[1]) & set(curInput[2]))
  # print(intersects)
  for c in intersects:
    ascii = ord(c)
    if ascii in range(ord("a"), ord("z") + 1):
      sumBadges += ascii - 96
    elif ascii in range(ord("A"), ord("Z") + 1):
      sumBadges += ascii - 38

print(sumBadges)