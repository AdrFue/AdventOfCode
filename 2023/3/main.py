import os 
from pprint import pprint

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[1], "r") as f:
    for line in f:
      lines.append(line.strip())

# print(lines)
digit_hit = False
dig = []
symbols = set()

for row in range(0, len(lines)):
    for char in range(0, len(lines[row])):
        if lines[row][char].isdigit():
            if digit_hit == False:
                dig.append([])
                dig[-1].append([row, char])
            digit_hit = True
        else:
            if digit_hit == True:
                dig[-1].append([row, char])
            digit_hit = False

            if not lines[row][char] == ".": # if not digit or . -> symbol
                symbols.add(lines[row][char])
    if digit_hit: # if digit is last value in row, ending has to be added seperatly
        dig[-1].append([row, 140])

result1 = 0

for d in dig:
    valid = False
    for i in range(d[0][1], d[1][1]):
        for s in symbols:
            if not d[0][0] == 0:
                if not i == 0:
                    if lines[d[0][0]-1][i-1] == s:
                        valid = True
                if lines[d[0][0]-1][i] == s:
                    valid = True 
                if not i == len(lines[0])-1:
                    if lines[d[0][0]-1][i+1] == s:
                        valid = True
            
            if not i == 0:    
                if lines[d[0][0]][i-1] == s:
                    valid = True
            if not i == len(lines[0])-1:
                if lines[d[0][0]][i+1] == s:
                    valid = True

            if not d[0][0] == len(lines)-1: 
                if not i == 0:
                    if lines[d[0][0]+1][i-1] == s:
                        valid = True
                if lines[d[0][0]+1][i] == s:
                    valid = True  
                if not i == len(lines[0])-1:
                    if lines[d[0][0]+1][i+1] == s:
                        valid = True
    if valid:
        value = ""
        for i in range(d[0][1], d[1][1]):
          value += lines[d[0][0]][i]
        
        result1 += int(value)

print(result1)