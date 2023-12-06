import os 
from pprint import pprint
import math

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[1], "r") as f:
    for line in f:
    	lines.append(line.strip())

print("Lines:", lines)
print("="*80)
data = []
for line in lines:
    data.append(line.split())
    data[len(data)-1].pop(0)


def solve(d):
    result = []

    for race in d:
        print(race)
        beaten = 0
        time = int(race[0])

        for i in range(time+1):
            covered_route = i*(time-i)
            if covered_route > int(race[1]):
                beaten += 1
        print(beaten)
        result.append(beaten)

    return result

## Part 1
print("Data:", data)
data_t = list(map(list, zip(*data))) # Transposing
print("Data:", data)
print("="*80)

result1 = solve(data_t)

print("="*80)
print(math.prod(result1))
print("="*80)

## Part 2
print(data)
data_j = []
data_j.append(["".join(d) for d in data])
result2 = solve(data_j)

print("="*80)
print(result2[0])
print("="*80)