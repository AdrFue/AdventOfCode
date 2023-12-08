import os 
import math
with open(os.path.dirname(os.path.realpath(__file__)) + "\\input1.txt", "r") as f:
    lines = [line.strip() for line in f]
def solve(d):
    return [sum(1 for i in range(int(race[0]) + 1) if i * (int(race[0]) - i) > int(race[1])) for race in d]
print(math.prod(solve(list(map(list, zip(*[line.split()[1:] for line in lines])))))) ## Part 1
print(solve([["".join(d) for d in [line.split()[1:] for line in lines]]])[0]) ## Part 2