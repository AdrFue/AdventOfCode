import os 
from pprint import pprint

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[0], "r") as f:
    for line in f:
    	lines.append(line.strip())

data = [[int(l) for l in line.split()] for line in lines]
pprint(data)
print("="*80)

result1 = 0
for d in data:
    calc_list = []
    calc_list.append(d)
    c = 0
    while True:
        cur_list = []
        for i in range(len(calc_list[c])-1):
            cur_list.append(calc_list[c][i+1] - calc_list[c][i])

        calc_list.append(cur_list)
        if sum(calc_list[c+1]) == 0 and calc_list[c+1][0] == 0:
            break
        c += 1

    calc_list = calc_list[::-1]
    for cl in calc_list:
        print(cl)


    cur_val = 0
    for i in range(len(calc_list)):
        cur_val += calc_list[i][len(calc_list[i])-1]
    print(cur_val)
    print("="*80)

    result1 += cur_val
print("="*80)
print(result1)