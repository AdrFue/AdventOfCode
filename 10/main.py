## Teil 1 ##

import os 
import numpy as np
dir = os.path.dirname(os.path.realpath(__file__))
lines = []

with open(dir + "/input.txt", "r") as f:
    for line in f:
      lines.append(line.strip())

X = 1
cycle = 0
i = 0
sigStrength = 0
watingCycle = True

while i < len(lines):
  cycle += 1
 
  if (cycle-20) % 40 == 0:
    sigStrength += cycle * X

  if lines[i].startswith('addx'):
    if watingCycle:
      watingCycle = False
      continue
    else:
      watingCycle = True
      X += int(lines[i].split(' ')[1])
      i += 1
  else:
    i += 1

print(sigStrength)


## Teil 2 ##

X = 1
cycle = 0
i = 0
sigStrength = 0
watingCycle = True

CRT = np.full((6, 40), " ")
print(CRT)

while i < len(lines):
  cycle += 1
  row = (cycle -1) // 40
  col1 = (X -1) % 40
  col2 = (X) % 40
  col3 = (X +1) % 40
  cyc2 = cycle % 40

  if col1 == cyc2-1 or col2 == cyc2-1 or col3 == cyc2-1:
    CRT[row][cyc2-1] = '#'

  if lines[i].startswith('addx'):
    if watingCycle:
      watingCycle = False
      continue
    else:
      watingCycle = True
      X += int(lines[i].split(' ')[1])
      i += 1
  else:
    i += 1

print(CRT)
CRTString = []
for row in CRT:
  CRTString.append(''.join(row))
f = open(dir + "/lsgWort.txt", "w")
f.write(str(CRTString))
f.close()