## Teil 1 ##

import os 
import numpy as np
dir = os.path.dirname(os.path.realpath(__file__))
lines = []

with open(dir + "/input.txt", "r") as f:
    for line in f:
      lines.append(line.strip())

# print(lines)

r = [int(x[2:]) for x in lines if x.startswith("R")]
d = [int(x[2:]) for x in lines if x.startswith("D")]
l = [int(x[2:]) for x in lines if x.startswith("L")]
u = [int(x[2:]) for x in lines if x.startswith("U")]
field = np.zeros((sum(u)+sum(d)+1, sum(r)+sum(l)+1))
print(field)
xH = len(field[0]) // 2
yH = len(field) // 2
xT = len(field[0]) // 2
yT = len(field) // 2
field[yT][xT] = 1

for i in lines:
  # print()
  # print(i)
  if i.startswith("R"):
      for j in range(int(i[2:])):
          xH += 1
          if (abs(xH-xT) >= 2 and abs(yH-yT) == 0 \
            or abs(xH-xT) == 0 and abs(yH-yT) >= 2) \
            or abs(xH-xT) + abs(yH-yT) >= 3:
            xT += 1
            yT = yH
            field[yT][xT] = 1
  elif i.startswith("U"):
      for j in range(int(i[2:])):
          yH -= 1
          if (abs(xH-xT) >= 2 and abs(yH-yT) == 0 \
            or abs(xH-xT) == 0 and abs(yH-yT) >= 2) \
            or abs(xH-xT) + abs(yH-yT) >= 3:
            yT -= 1
            xT = xH
            field[yT][xT] = 1
  elif i.startswith("L"):
      for j in range(int(i[2:])):
          xH -= 1
          if (abs(xH-xT) >= 2 and abs(yH-yT) == 0 \
            or abs(xH-xT) == 0 and abs(yH-yT) >= 2) \
            or abs(xH-xT) + abs(yH-yT) >= 3:
            xT -= 1
            yT = yH
            field[yT][xT] = 1
  elif i.startswith("D"):
      for j in range(int(i[2:])):
          yH += 1
          if (abs(xH-xT) >= 2 and abs(yH-yT) == 0 \
            or abs(xH-xT) == 0 and abs(yH-yT) >= 2) \
            or abs(xH-xT) + abs(yH-yT) >= 3:
            yT += 1
            xT = xH
            field[yT][xT] = 1

  # print("head:", xH, yH, "tail:", xT, yT)
  # print(field)

print(np.sum(field))
