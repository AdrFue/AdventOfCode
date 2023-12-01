## Teil 2 ##
## NOT YET WORKING ##

import os 
import numpy as np
dir = os.path.dirname(os.path.realpath(__file__))
lines = []

with open(dir + "/inputSmall2.txt", "r") as f:
    for line in f:
      lines.append(line.strip())

# print(lines)

r = [int(x[2:]) for x in lines if x.startswith("R")]
d = [int(x[2:]) for x in lines if x.startswith("D")]
l = [int(x[2:]) for x in lines if x.startswith("L")]
u = [int(x[2:]) for x in lines if x.startswith("U")]
field = np.zeros((max(sum(u), sum(d))+1, max(sum(r), sum(l))+1))
# print(field)
xH = len(field[0]) // 2 +1
yH = len(field) // 2 +1
xTs = np.full((9), len(field[0]) // 2 +1)
yTs = np.full((9), len(field) // 2 +1)
print("head:", xH, yH, "tail:", xTs, yTs)
field[yTs[8]][xTs[8]] = 1

def moveTail(dir, lXH, lYH, lXT, lYT, last):
  # print("moveTail", lXH, lXT, lYH, lYT)
  if (abs(lXH-lXT) >= 2 and abs(lYH-lYT) == 0 \
    or abs(lXH-lXT) == 0 and abs(lYH-lYT) >= 2) \
    or abs(lXH-lXT) + abs(lYH-lYT) >= 3:
    match dir:
      case "R":
        lXT += 1
        lYT = lYH
      case "U":
        lYT -= 1
        lXT = lXH
      case "L":
        lXT -= 1
        lYT = lYH
      case "D":
        lYT += 1
        lXT = lXH    
    if last:
      field[lYT][lXT] = 1
  return lXT, lYT

def callMoveTail(dir):
  xTs[0], yTs[0] = moveTail(dir, xH, yH, xTs[0], yTs[0], 0)
  for i in range(1, len(xTs)-1): # going through all tail values
    xTs[i], yTs[i] = moveTail(dir, xTs[i-1], yTs[i-1], xTs[i], yTs[i], 0)
  xTs[len(xTs)-1], yTs[len(xTs)-1] = moveTail(dir, xTs[len(xTs)-2], yTs[len(xTs)-2], xTs[len(xTs)-1], yTs[len(xTs)-1], 1) # 1 == last values will be moved
    

for i in lines:
  print()
  print(i)
  if i.startswith("R"):
    for j in range(int(i[2:])): 
      xH += 1
      callMoveTail("R")

  elif i.startswith("U"):
    for j in range(int(i[2:])):
      yH -= 1
      callMoveTail("U")

  elif i.startswith("L"):
    for j in range(int(i[2:])):
      xH -= 1
      callMoveTail("L")

  elif i.startswith("D"):
    for j in range(int(i[2:])):
      yH += 1
      callMoveTail("D")

  print("head:", xH, yH, "tail:", xTs, yTs)
  # print(field)

print(np.sum(field))
