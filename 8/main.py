## Teil 1 ##

import os 
from pprint import pprint
import numpy as np
dir = os.path.dirname(os.path.realpath(__file__))
inputs = []

with open(dir + "/input.txt", "r") as f:
    for line in f:
      inputs.append(line.strip())

def getVisiblesTrees(forest, vArray):
  vt = 0
  for row in range(len(forest)):
    highestTree = -1
    for column in range(len(forest[row])):
      if forest[row][column] > highestTree:
        highestTree = forest[row][column]
        if vArray[row][column] == 0:
          vArray[row][column] = 1
          vt += 1
 
  return vt

forest = []
visibleTrees = 0
for row in inputs:
  forest.append([int(char) for char in row])
vtArray = np.zeros((len(forest), len(forest[0])))

# counting left to right
print("left to right ------------------")
visibleTrees += getVisiblesTrees(forest, vtArray)

# transpose forest --> counting top to bottom
print("top to bottom ------------------")
forest = np.array(forest).T.tolist()
vtArray = np.array(vtArray).T.tolist()
visibleTrees += getVisiblesTrees(forest, vtArray)

# reverse forest --> counting bottom to top
print("bottom to top ------------------")
for row in forest:
  row.reverse()
for row in vtArray:
  row.reverse()
visibleTrees += getVisiblesTrees(forest, vtArray)

# transpose forest --> counting right to left
print("right to left ------------------")
forest = np.array(forest).T.tolist()
vtArray = np.array(vtArray).T.tolist()
for row in forest:
  row.reverse()
for row in vtArray:
  row.reverse()
visibleTrees += getVisiblesTrees(forest, vtArray)
print(visibleTrees)





