## Teil 1 ##

import os 
dir = os.path.dirname(os.path.realpath(__file__))
inputs = []

with open(dir + "/input.txt", "r") as f:
    for line in f:
        inputs.append(line)

values = []
for input in inputs:
  curLine = input.split(" ")
  curLine[1] = curLine[1].replace('\n', '')
  values.append(curLine)
print(values)

# A = X = Rock     = 1
# B = Y = Paper    = 2
# C = Z = Scissors = 3
# Win  = 6
# Draw = 3,0
# Loss = 0

score = 0

for value in values:
  if value[0] == "A": # Rock
    if value[1] == "X": # Rock vs Rock
      score += 3 + 1
    elif value[1] == "Y": # Rock vs Paper
      score += 6 + 2
    elif value[1] == "Z": # Rock vs Scissors
      score += 0 + 3

  elif value[0] == "B": # Paper
    if value[1] == "X": # Paper vs Rock
      score += 0 + 1
    elif value[1] == "Y": # Paper vs Paper
      score += 3 + 2
    elif value[1] == "Z": # Paper vs Scissors
      score += 6 + 3

  elif value[0] == "C": # Scissors
    if value[1] == "X": # Scissors vs Rock
      score += 6 + 1
    elif value[1] == "Y": # Scissors vs Paper
      score += 0 + 2
    elif value[1] == "Z": # Scissors vs Scissors
      score += 3 + 3

print(score)


## Teil 2 ##

# A = Rock     = 1
# B = Paper    = 2
# C = Scissors = 3
# Win  = 6 = Z
# Draw = 3 = Y
# Loss = 0 = X

score = 0

for value in values:
  if value[0] == "A": # Rock
    if value[1] == "X": # Loss with Scissors
      score += 0 + 3
    elif value[1] == "Y": # Draw with Rock
      score += 3 + 1
    elif value[1] == "Z": # Win with Paper
      score += 6 + 2

  elif value[0] == "B": # Paper
    if value[1] == "X": # Loss with Rock
      score += 0 + 1
    elif value[1] == "Y": # Draw with Paper
      score += 3 + 2
    elif value[1] == "Z": # Win with Scissors
      score += 6 + 3

  elif value[0] == "C": # Scissors
    if value[1] == "X": # Loss with Paper
      score += 0 + 2
    elif value[1] == "Y": # Draw with Scissors
      score += 3 + 3
    elif value[1] == "Z": # Win with Rock
      score += 6 + 1

print(score)

