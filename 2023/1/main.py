import os 
import re

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[3], "r") as f:
    for line in f:
      lines.append(line.strip())

## Part 1
def solve(lines):
    res = 0
    for line in lines:
        digits = re.findall(r'\d+', line)
        val = int(digits[0][0] + digits[-1][-1])
        res += val
    return res

print(solve(lines))

## Part 2

help_dict = {
    'one': 'o1e',
    'two': 't2o',
    'three': 'th3ee',
    'four': 'f4ur',
    'five': 'f5ve',
    'six': 's6x',
    'seven': 'se7en',
    'eight': 'ei8ht',
    'nine': 'n9ne'
}

new_lines = []
for line in lines:
    res = line
    for key in help_dict:
        res = res.replace(key, help_dict[key])
    new_lines.append(res)

print(solve(new_lines))


      