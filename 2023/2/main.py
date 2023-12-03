import os 
import re
import pandas as pd

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[1], "r") as f:
    for line in f:
      lines.append(line.strip())


result1 = 0
result2 = 0

for i in range(0, len(lines)):
    line = lines[i][lines[i].find(": ")+2:]
    to_big = False
    games = line.split("; ")
    maxRed = 1
    maxGreen = 1
    maxBlue = 1
    for g in games:
        cubes = g.split(", ")
        for c in cubes:
            val = c.split(" ")

            # Part 1
            if val[1] == "red" and int(val[0]) > 12 or val[1] == "green" and int(val[0]) > 13 or val[1] == "blue" and int(val[0]) > 14:
                to_big = True

            # Part 2
            if val[1] == "red" and int(val[0]) > maxRed:
                maxRed = int(val[0])
            if val[1] == "blue" and int(val[0]) > maxBlue:
                maxBlue = int(val[0])
            if val[1] == "green" and int(val[0]) > maxGreen:
                maxGreen = int(val[0])


    # Part 1            
    print(i+1, to_big)
    print(games)
    if not to_big:
        result1 += i+1

    # Part 2
    print(maxRed, maxBlue, maxGreen, maxRed*maxBlue*maxGreen)
    result2 += maxRed*maxBlue*maxGreen

print(result1)
print(result2)
