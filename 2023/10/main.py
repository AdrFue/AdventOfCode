import os 
from pprint import pprint

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[0], "r") as f:
    for line in f:
    	lines.append(line.strip())

for line in lines:
    print(line)
print()

def check_above(row, column):
    if row > 0:
        if lines[row-1][column] == '|' or lines[row-1][column] == '7' or lines[row-1][column] == 'F' or lines[row-1][column] == 'S':
            cons[row][column] += 1

def check_below(row, column):
    if row < len(lines)-1:
        if lines[row+1][column] == '|' or lines[row+1][column] == 'J' or lines[row+1][column] == 'L' or lines[row+1][column] == 'S':
            cons[row][column] += 1
    
def check_left(row, column):
    if column > 0:
        if lines[row][column-1] == '-' or lines[row][column-1] == 'L' or lines[row][column-1] == 'F' or lines[row][column-1] == 'S': 
            cons[row][column] = cons[row][column] + 1

def check_right(row, column):
    if column < len(lines[0])-1:
        if lines[row][column+1] == '-' or lines[row][column+1] == 'J' or lines[row][column+1] == '7' or lines[row][column+1] == 'S': 
            cons[row][column] += 1

def check_sur(v, r, c):
    if v in 'J|L':
        check_above(r, c)
    if v in '7|F':
        check_below(r, c)
    if v in '7-J':
        check_left(r, c)
    if v in 'F-L':
        check_right(r, c)

cons = [[0] * len(lines[0]) for _ in range(len(lines))] 
for i, row in enumerate(lines):
    for j, value in enumerate(row):
        if value == 'S':
            cons[i][j] == -1
        if value != '.':
            check_sur(value, i, j)

for c in cons:
    print(c)
print("="*80)
            
