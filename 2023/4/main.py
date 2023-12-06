import os 
from pprint import pprint
import math
import numpy as np

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[1], "r") as f:
    for line in f:
    	lines.append(line.strip())


data = []
for line in lines:
    data.append(line.replace("  ", " ").split(": ")[1])

cards = [d.split(" | ") for d in data]

games = []
for card in cards:
    games.append([c.split(" ") for c in card])

## Part 1
result1 = 0
for game in games:
    wins = len(set(game[0]) & set(game[1]))
    # print(wins, math.floor(2**(wins-1)), game)
    result1 += math.floor(2**(wins-1))
print(result1)


## Part 2
scs = np.ones(len(games))
for i in range(len(games)):
    wins = len(set(games[i][0]) & set(games[i][1]))
    for j in range(1, wins+1):
        scs[i+j] += 1 * scs[i]

print(int(sum(scs)))