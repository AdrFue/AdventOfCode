import os 
from pprint import pprint

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[1], "r") as f:
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

found = False
cur_node = 0
cur_dir = 0
steps = 0
cur_val = 'AAA'
while not (found):
    if cur_dir >= len(dirs):
        cur_dir = 0
    steps += 1
    dir = dirs[cur_dir]
    cur_node = nodes.index(cur_val)
    cur_val = data[cur_node][int(dir)]
    print(cur_val)
    if cur_val == 'ZZZ':
        found = True

    cur_dir +=1

print(steps)