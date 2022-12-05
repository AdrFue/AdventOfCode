## Teil 1 ##

import os 
dir = os.path.dirname(os.path.realpath(__file__))
inputs = []

with open(dir + "/input.txt", "r") as f:
    for line in f:
      inputs.append(line.strip())

inpSplits = []
for input in inputs:
  inpSplits.append(input.split(','))

values = []
for i in range(len(inpSplits)):
  values.append([])
  for inpSplit in inpSplits[i]:
    values[i].append(inpSplit.split('-'))

assignments = 0
for value in values:
  if (int(value[0][0]) <= int(value[1][0]) and int(value[0][1]) >= int(value[1][1]) or 
      int(value[0][0]) >= int(value[1][0]) and int(value[0][1]) <= int(value[1][1])):
    assignments += 1

print(assignments)


## Teil 2 ##

overlaps = 0
for value in values:
  if int(value[0][1]) >= int(value[1][0]) and int(value[0][0]) <= int(value[1][1]): 
    overlaps += 1

print(overlaps)