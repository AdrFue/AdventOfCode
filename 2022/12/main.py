## Teil 1 ##
# FUNZT NOCH NICHT

import os 
from pprint import pprint
import numpy as np
import sys
sys.setrecursionlimit(10000)

def route(r,c,d,p):
  d += 1
  p[r][c] = 1

  print("r:", r, "c:", c, "d:", d)

  # Ziel erreicht
  if r == rFinal and c == cFinal:
    finalDis.append(d-1)
    return 
  
  # rechts
  if c < len(npMap[0])-1:
    if abs(npMap[r][c+1] - npMap[r][c]) <= 1 and p[r][c+1] == 0:
      # p[r][c+1] = 1
      route(r, c+1, d, p)

  # unten
  if r < (len(npMap)-1):
    if abs(npMap[r+1][c] - npMap[r][c]) <= 1 and p[r+1][c] == 0:
      # p[r+1][c] = 1
      route(r+1, c, d, p)

  # oben
  if r > 0:
    if abs(npMap[r-1][c] - npMap[r][c]) <= 1 and p[r-1][c] == 0:
      # p[r-1][c] = 1
      route(r-1, c, d, p)

  # links
  if c > 0:
    if abs(npMap[r][c-1] - npMap[r][c]) <= 1 and p[r][c-1] == 0:
      # p[r][c-1] = 1
      route(r, c-1, d, p)


dir = os.path.dirname(os.path.realpath(__file__))
lines = []
with open(dir + "/input.txt", "r") as f:
    for line in f:
      lines.append(line.strip())

map = []
for line in lines:
  map.append([ord(char)-96 for char in line])
npMap = np.array(map)


rStart = np.where(npMap == -13)[0][0]
cStart = np.where(npMap == -13)[1][0]
rFinal = np.where(npMap == -27)[0][0]
cFinal = np.where(npMap == -27)[1][0]

npMap[rFinal][cFinal] = 26
prevSeen = np.zeros((len(npMap), len(npMap[0])))

npMap[rStart][rStart] = 1
prevSeen[rStart][rStart] = 1

finalDis = []
route(rStart, rStart, 0, prevSeen)
print("finale Distanzen:", finalDis)
# print("min:", min(finalDis))

