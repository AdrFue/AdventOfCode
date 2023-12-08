import os 
from pprint import pprint
import math

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[3], "r") as f:
    for line in f:
    	lines.append(line.strip())

dirs = lines[0]
dirs = dirs.replace("L", "0")
dirs = dirs.replace("R", "1")
nodes = [line.split()[0] for line in lines[2:]]
data = [line.split('(')[1] for line in lines[2:]]
data = [d[:-1].split(', ') for d in data]
# print(dir)
# pprint(nodes)
# pprint(data)
# print("="*80)

cur_vals = [i for i in range(len(nodes)) if nodes[i][-1] == 'A']
for i, sp in enumerate(cur_vals):
    cur_vals[i] = nodes[sp]
steps = [0] * len(cur_vals)

for i in range(len(cur_vals)):
    found = False
    cur_node = 0
    cur_dir = 0
    cur_val = cur_vals[i]
    while not (found):
        if cur_dir >= len(dirs):
            cur_dir = 0
        steps[i] += 1
        dir = dirs[cur_dir]
        cur_node = nodes.index(cur_val)
        cur_val = data[cur_node][int(dir)]
        if cur_val[-1] == 'Z':
            found = True
        cur_dir +=1

# print(steps)
print(math.lcm(*steps))