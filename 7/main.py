## Teil 1 ##

import os 
dir = os.path.dirname(os.path.realpath(__file__))
inputs = []

with open(dir + "/input.txt", "r") as f:
    for line in f:
      inputs.append(line.strip())
  
dirs = []
dirSizes = {}
dirSizes["/"] = 0
dirs.append("/")

for input in inputs:

  if input.startswith("$ cd"):
    if input.startswith("$ cd .."):
      dirs.pop()
    elif input.startswith("$ cd /"):
      dirs = ["/"]
    else:
      dirs.append(dirs[-1]+input[5:])
      
  if input[0].isdigit():
    for dir in dirs:
      if dir not in dirSizes:
        dirSizes[dir] = 0
      dirSizes[dir] += int(input.split(" ")[0])

sumDirs = 0
for (key, value) in dirSizes.items():
  if value <= 100_000:
    sumDirs += value

print(sumDirs)


## Teil 2 ##

dirSizesSorted = sorted(dirSizes.items(), key=lambda x: x[1])
reqSpace = 30_000_000 - (70_000_000 - dirSizes["/"])

for (key, value) in dirSizesSorted:
  if value > reqSpace:
    print(key, value)
    break
