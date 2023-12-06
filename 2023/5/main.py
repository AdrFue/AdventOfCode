import os 
from pprint import pprint
from time import time


dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[1], "r") as f:
    for line in f:
    	lines.append(line.strip())

map_lines = []
for i, line in enumerate(lines):
    print(i, line)
    if line.find(":") >= 0:
        map_lines.append(i+1)
print("="*80)

def mapper(cur_line, seeds):
    sts = []
    while(True):  
        if cur_line >= len(lines):
            break
        if lines[cur_line] == '' :
            break
        st = lines[cur_line].split()
        st = [int(s) for s in st]
        sts.append(st)

        cur_line += 1

    for i, seed in enumerate(seeds):
        for st in sts:
            if seed in range(st[1], st[1]+st[2]):
                print(seed, st)
                seeds[i] += st[0] - st[1]
                print("Hit! New Seed: ", seed)

    print(seeds)
    print("="*80)
    return seeds

## Part 1
my_seeds1 = lines[0].split(":")[1].split()
my_seeds1 = [int(seed) for seed in my_seeds1]
print(my_seeds1)

for ml in map_lines:
    print("CurLine: ", ml)
    my_seeds1 = mapper(ml, my_seeds1)
print(min(my_seeds1))

print("="*80)
print("="*80)

## Not Working Part 2
my_seeds2 = lines[0].split(":")[1].split()
work_list = [my_seeds2[ms:ms+2] for ms in range(0, len(my_seeds2),2)]
print(work_list)
my_seeds2 = []
for pair in work_list:
    for i in range(int(pair[1])):
        my_seeds2.append(int(pair[0])+i)

start = time()
print(my_seeds2)
for ml in map_lines:
    print("CurLine: ", ml)
    my_seeds2 = mapper(ml, my_seeds2)
print(min(my_seeds2))
print("Duration:", time()-start())
