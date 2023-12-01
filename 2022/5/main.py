## Teil 1 ##

import os 
dir = os.path.dirname(os.path.realpath(__file__))
inputs = []

crates = [
  ["H", "C", "R"],
  ["B", "J", "H", "L", "S", "F"],
  ["R", "M", "D", "H", "J", "T", "Q"],
  ["S", "G", "R", "H", "Z", "B", "J"],
  ["R", "P", "F", "Z", "T", "D", "C", "B"],
  ["T", "H", "C", "G"],
  ["S", "N", "V", "Z", "B", "P", "W", "L"],
  ["R", "J", "Q", "G", "C"],
  ["L", "D", "T", "R", "H", "P"," F", "S"]
]

with open(dir + "/input.txt", "r") as f:
    for line in f:
      inputs.append(line.strip())

cmds = []
for input in inputs:
  cmds.append(input.replace('move', '').replace('from', '').replace('to', '').strip().split('  '))
  cmds[len(cmds)-1][0] = int(cmds[len(cmds)-1][0])
  cmds[len(cmds)-1][1] = int(cmds[len(cmds)-1][1]) -1
  cmds[len(cmds)-1][2] = int(cmds[len(cmds)-1][2]) -1
  
for cmd in cmds:
  for i in range(cmd[0]):
    crates[cmd[2]].append(crates[cmd[1]][len(crates[cmd[1]])-1])
    crates[cmd[1]].pop()

for crate in crates:
  print(crate[len(crate)-1], end='')
print()


## Teil 2 ##

crates = [
  ["H", "C", "R"],
  ["B", "J", "H", "L", "S", "F"],
  ["R", "M", "D", "H", "J", "T", "Q"],
  ["S", "G", "R", "H", "Z", "B", "J"],
  ["R", "P", "F", "Z", "T", "D", "C", "B"],
  ["T", "H", "C", "G"],
  ["S", "N", "V", "Z", "B", "P", "W", "L"],
  ["R", "J", "Q", "G", "C"],
  ["L", "D", "T", "R", "H", "P"," F", "S"]
]

for cmd in cmds:
  crateMover = crates[cmd[1]][-cmd[0]:]
  del crates[cmd[1]][-cmd[0]:]
  for crate in crateMover:
    crates[cmd[2]].append(crate)

for crate in crates:
  print(crate[len(crate)-1], end='')