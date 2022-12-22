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
  # print(cycle, ":", X, "(", lines[i], ")")

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
